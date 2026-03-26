# Before Thursday: Install Claude Code

Hi everyone,

This Thursday (Feb 26) we'll be introducing **Claude Code** -- an AI-powered terminal assistant that will help you with data cleaning, coding, and managing your capstone projects for the rest of the semester.

**Please install it before class** so we can hit the ground running. It takes about 10 minutes.

---

## Step 1: Install Claude Code

Follow the official install instructions here: **https://docs.anthropic.com/en/docs/claude-code/overview**

The page walks you through everything -- just follow the steps for your operating system (Mac, Linux, or Windows via WSL).

Once installed, verify it works:

```bash
claude --version
```

You should see a version number.

**Windows users:** Claude Code works best in a Unix-like terminal. If you don't already have WSL (Windows Subsystem for Linux), install it first: https://learn.microsoft.com/en-us/windows/wsl/install

## Step 2: API Access

**You don't need to buy anything.** I'll be sending each of you a **3-month Claude Pro subscription**, which includes Claude Code access. You'll receive an email with instructions to activate it.

Once your Pro subscription is active, Claude Code will work automatically -- no separate API key needed.

## Step 3: Test It

```bash
cd ~/path/to/your-capstone-repo
claude
```

When it launches for the first time, it will ask for your API key. Paste it in.

Then try:

```
> What files are in this directory?
```

If Claude Code responds with a list of your files, you're all set!

Type `/exit` to quit.

---

## What We'll Do in Class

- Set up a `CLAUDE.md` file that teaches Claude Code about your specific project
- Learn best practices for data cleaning and reproducible pipelines
- Use Claude Code to clean and merge your actual capstone data
- Hands-on work sprint with your own datasets

**Bring your laptop with your capstone repository ready to go.** If your data is on a remote server, make sure you can access it from your laptop.

---

## Troubleshooting

If you run into issues, check the install page linked above for troubleshooting tips. If you're still stuck, post in the discussion board or email me and we'll sort it out at the start of class.

See you Thursday!

Andrew
