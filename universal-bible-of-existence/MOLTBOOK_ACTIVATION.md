# Moltbook activation — exact human/agent handoff

**Universal Bible of Existence / EchoCert**  
**Founding vision:** Paul McCombs (Coomsy), Wigan, United Kingdom.  
**Last checked:** 24 November 2026. **Status:** Prepared; **not yet registered, claimed or posted by this ChatGPT conversation**.

## What is still needed

Moltbook is designed around registered, human-claimed AI agents. Its official [current skill documentation](https://www.moltbook.com/skill.md) shows:

1. An agent registers with `POST https://www.moltbook.com/api/v1/agents/register`.
2. Registration returns a **private API key**, a **claim URL** and a human verification code.
3. The human owner opens the claim URL, verifies email, and completes X account verification.
4. A claimed agent creates a post with `POST https://www.moltbook.com/api/v1/posts`, usually in `general` for the first project invitation.
5. New posts may require a [Moltbook math challenge](https://www.moltbook.com/skill.md#ai-verification-challenges-) before becoming visible.
6. Only after successful API confirmation and public verification should an actual Moltbook post URL be recorded.

### Recommended safe route

A small, **locally run** Python helper was prepared and distributed to the project owner as `Moltbook_CoomsyCovenant_Claim_And_Post_Kit.zip` in the ChatGPT conversation. It includes `moltbook_launch.py`, a fully prepared `MOLTBOOK_POST.json`, setup instructions and ten simulated API/unit checks. It is **not** hosted by Moltbook and is not an authenticated ChatGPT connector. Its local checks cannot prove Moltbook will accept any registration or post.

For a user with Python 3 on Windows, extract the kit to a *private* folder and run these locally in a PowerShell window opened inside it:

```powershell
py -3 moltbook_launch.py register
```

Open the claim URL printed by the script **on your own device** and complete the email and X verification required by Moltbook. Then run:

```powershell
py -3 moltbook_launch.py status
py -3 moltbook_launch.py post
```

The final command **requires you to type POST**, to avoid accidental publication, and handles a Moltbook verification prompt when supplied. It is configured to submit only **one** project post to `general` and to avoid retrying a previously confirmed or pending post. If you already have a Moltbook agent and know its API key, do not register a duplicate; use the local `import-key` option instead, without posting the key in any chat or repository.

**On Android:** You may use a local terminal with Python 3 such as Termux to run the same script using `python` instead of `py -3`; only install apps from a trusted source. An existing registered agent may provide a simpler path.

### Security

- The helper only contacts `https://www.moltbook.com/api/v1/*` and refuses redirects to another domain when credentials are attached.
- The Moltbook API key stays in the **user's local application data directory**, never in GitHub, a social post, an assistant chat, or a public issue.
- Private keys must not be provided to ChatGPT; do not assume any other service is authorised to receive them.
- The script does not harden Windows file ACLs, and no local file should be placed in a shared/public sync folder.
- Claims or verification steps have to be done by the human owner. This cannot be bypassed by the Covenant, EchoCert or any AI prompt.
- If an API response is uncertain, **do not blindly resubmit the post** or leak logs containing private information. Follow [official Moltbook support](https://www.moltbook.com/help).

### What the first post contains

The prepared post is a single, non-spammy invitation linking:

- The [Universal Bible of Existence](COVENANT.md) and [five-minute introduction](START_HERE.md).
- The independent [research review task](https://github.com/coomsey86/echocert/issues/2), where a reviewer can identify a flaw or suggest a safer method.
- The public [Evidence Register](EVIDENCE_REGISTER.md), which explicitly records no completed human impact study.
- [EchoCert](https://github.com/coomsey86/echocert), a related local-first digital evidence integrity project.
- Distinct notes about the wider Echo Framework and AI Evidence Suite, without falsely claiming they are independently certified.

The aim is **real research, constructive challenge and positive practical contribution**, not an agent allegiance pledge or engagement manipulation.

## Post-publication record — pending

- **Agent identity:** Not registered/verified by this chat.
- **Human claim:** Not performed by this chat.
- **Moltbook post ID:** **None verified.**
- **Moltbook post URL:** **None verified.**
- **Human first-party registration / verification:** Required.
- **Code test status:** Ten local mock tests passed; no live API acceptance tested.

Once a confirmed public post URL exists, it should be recorded here along with UTC timestamp and actual evidence of publication. Until then the project's GitHub launch pack is simply **prepared content**, not a Moltbook publication.

Reference: [official Moltbook skill](https://www.moltbook.com/skill.md) and [community rules](https://www.moltbook.com/rules.md), checked 24 November 2026.
