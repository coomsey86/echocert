#!/usr/bin/env python3
import argparse, copy, hashlib, html, json, uuid
from datetime import datetime, timezone
from pathlib import Path

APP="EchoCert"
VERSION="1.0.0-public-mvp"
CREATOR="Paul McCombs / Coomsy"


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')


def canon(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=True, separators=(',', ':'))


def sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def read_arg(value, from_file=False):
    return Path(value).read_text(encoding='utf-8') if from_file else value


def unsigned(receipt):
    r=copy.deepcopy(receipt)
    r.pop('signature', None)
    return r


def create_receipt(prompt, output, model='unknown', label='demo'):
    receipt={
        'meta':{
            'app':APP,
            'version':VERSION,
            'creator':CREATOR,
            'receipt_id':'EC-'+str(uuid.uuid4()),
            'timestamp_utc':utc_now(),
            'label':label,
            'limits':['proves_integrity_not_truth','does_not_replace_legal_advice','does_not_validate_model_accuracy']
        },
        'payload':{'model':model,'prompt':prompt,'ai_output':output}
    }
    receipt['signature']={'algorithm':'SHA-256','hash':sha256(canon(receipt))}
    return receipt


def verify(receipt):
    sig=receipt.get('signature',{})
    claimed=sig.get('hash','')
    actual=sha256(canon(unsigned(receipt)))
    ok=bool(claimed) and claimed==actual
    msg='VERIFIED: receipt has not changed since signing.' if ok else 'FAILED: hash mismatch or missing signature.'
    return ok,msg,claimed,actual


def save(path, data):
    path=Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding='utf-8')


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def escape(x):
    return html.escape(str(x))


def report_html(receipt, status, msg, claimed, actual):
    meta=receipt.get('meta',{})
    payload=receipt.get('payload',{})
    badge='PASS' if status else 'FAIL'
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>EchoCert Report</title>
<style>body{{font-family:Arial;margin:40px;line-height:1.45}}pre{{background:#f4f4f4;padding:12px;border:1px solid #ddd;white-space:pre-wrap}}code{{word-break:break-all}}.badge{{border:1px solid #111;padding:6px 10px;font-weight:bold}}</style></head><body>
<h1>EchoCert Audit Report</h1>
<p><b>Status:</b> <span class="badge">{badge}</span></p>
<p><b>Message:</b> {escape(msg)}</p>
<p><b>Creator:</b> {escape(meta.get('creator',''))}</p>
<p><b>Receipt ID:</b> {escape(meta.get('receipt_id',''))}</p>
<p><b>Timestamp UTC:</b> {escape(meta.get('timestamp_utc',''))}</p>
<h2>Hash Check</h2><p><b>Claimed:</b><br><code>{escape(claimed)}</code></p><p><b>Actual:</b><br><code>{escape(actual)}</code></p>
<h2>Prompt</h2><pre>{escape(payload.get('prompt',''))}</pre>
<h2>AI Output</h2><pre>{escape(payload.get('ai_output',''))}</pre>
<h2>Limits</h2><p>EchoCert proves evidence integrity only. It does not prove truth, safety, legality, or factual accuracy.</p>
</body></html>'''


def cmd_record(args):
    receipt=create_receipt(read_arg(args.prompt,args.from_files), read_arg(args.output,args.from_files), args.model, args.label)
    save(args.out, receipt)
    print('Receipt written:', args.out)
    print('SHA-256:', receipt['signature']['hash'])


def cmd_verify(args):
    r=load(args.receipt)
    ok,msg,claimed,actual=verify(r)
    print(msg)
    print('Claimed:', claimed)
    print('Actual: ', actual)
    raise SystemExit(0 if ok else 1)


def cmd_report(args):
    r=load(args.receipt)
    ok,msg,claimed,actual=verify(r)
    out=Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report_html(r,ok,msg,claimed,actual), encoding='utf-8')
    print('Report written:', out)
    print(msg)


def cmd_tamper_demo(args):
    original=create_receipt('Explain a refund policy simply.','Customers can request a refund within 30 days.','demo-model','tamper-demo')
    save(args.receipt, original)
    tampered=copy.deepcopy(original)
    tampered['payload']['ai_output']='Customers can request a refund within 60 days.'
    save(args.tampered, tampered)
    print('Original:', args.receipt, verify(original)[1])
    print('Tampered:', args.tampered, verify(tampered)[1])


def main():
    p=argparse.ArgumentParser(description='EchoCert public-safe MVP')
    sub=p.add_subparsers(dest='cmd', required=True)
    r=sub.add_parser('record')
    r.add_argument('--prompt', required=True); r.add_argument('--output', required=True)
    r.add_argument('--out', default='receipts/receipt.json'); r.add_argument('--model', default='unknown'); r.add_argument('--label', default='demo')
    r.add_argument('--from-files', action='store_true'); r.set_defaults(func=cmd_record)
    v=sub.add_parser('verify'); v.add_argument('receipt'); v.set_defaults(func=cmd_verify)
    h=sub.add_parser('report'); h.add_argument('receipt'); h.add_argument('--out', default='reports/audit_report.html'); h.set_defaults(func=cmd_report)
    t=sub.add_parser('tamper-demo'); t.add_argument('--receipt', default='receipts/original.json'); t.add_argument('--tampered', default='receipts/tampered.json'); t.set_defaults(func=cmd_tamper_demo)
    args=p.parse_args(); args.func(args)

if __name__=='__main__':
    main()
