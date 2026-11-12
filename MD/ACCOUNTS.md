# Accounts: Login, Register, Guest

> Part of the REO docs. Code: `auth` script in `index.html` (`REO_AUTH`). **Status: local only. There is no game server yet.**

## 1. What a player sees

The first screen is a login page (Thai or English, with a switch; the default follows the browser language) with three tabs:

| Tab | Fields | What it does |
|---|---|---|
| **Login** | Username, Password, "Keep me signed in" | Logs into an account made on this browser |
| **Register** | Username, Character name, Password, Confirm password (+ strength bar, + "Move my guest progress" when a guest save exists) | Creates an account and enters the game |
| **Guest** | Nickname (optional) | Plays right away with no account |

- Players who already have a save from before accounts existed land on the **Guest** tab, with a note like "Found existing progress: Lv 24", so nothing is lost. Their old save becomes the guest save.
- A first-time visitor with no accounts lands on **Register**.
- Show/Hide password buttons, Enter to submit, and generic errors (see §3).

## 2. Rules

| Field | Rule |
|---|---|
| Username | 3–16 characters, `a-z A-Z 0-9 _`. Not case-sensitive for uniqueness (`Rowan_K` = `rowan_k`) |
| Character name | 2–12 characters: letters (Thai and Latin), numbers, `_`, `-`, spaces |
| Password | at least 6 characters (a strength bar shows Weak/Fair/Good/Strong) |
| Reserved names | `admin gm system moderator root guest mod staff support` (username and character name) |
| Guest nickname | same rules as a character name; if empty, `Guest` + 4 digits (kept for next time) |

## 3. Security (read this)

What is done:
- Passwords are **never stored in plain text**. Each account stores a random 16-byte salt and a **PBKDF2-SHA-256 hash (100,000 rounds)**. If the browser has no `crypto.subtle`, a salted SHA-256 chain (3,000 rounds) is used instead; accounts remember which method made them.
- Login errors are generic ("Wrong username or password"), the same for unknown names, and unknown names still pay the hashing cost.
- **5 wrong attempts lock that username for 30 s**, doubling for each further 5 (max 4 min). The counter survives reloads.
- Names are validated (no HTML can get in), and everything shown is escaped.
- "Keep me signed in" off = the session lasts for that tab only.

What is **not** secure, because there is no server:
- Accounts, hashes and saves live in this browser's `localStorage`. Anyone with access to the device and browser tools can read, copy or edit them, including the save (gold, items).
- Accounts do **not** follow the player to another browser or device. Clearing browser data deletes the account and its save.
- There is **no password reset**: nobody can verify who you are. The only way out of a forgotten password is to delete the data.
- The lockout can be bypassed by clearing storage.

So this is a convenience system for the prototype (separate saves, character names, a place to keep progress), not protection. Do not treat it as account security.

## 4. Where data is stored

| Key | Content |
|---|---|
| `reo.accounts.v1` | `{ users: { <lowercase name>: { id, name, charName, salt, hash, algo, created } } }` |
| `reo.save.<id>.v2` | the save of that account (same format as before) |
| `reo.gameState.v2` | the **guest** save (also where all pre-account saves are) |
| `reo.session.v1` | who is signed in (`localStorage`, or `sessionStorage` when "keep me signed in" is off) |
| `reo.auth.fails.v1`, `reo.lastUser`, `reo.guestName`, `reo.authLang` | lockout counters, prefilled username, guest nickname, login-page language |

## 4b. Inside the game
**Settings → Account** shows who is signed in and has:
- **Log out** (saves first, then returns to the login page).
- **Create an account (keep my progress)** for guests: opens Register with "Move my guest progress" ticked. The guest save is **copied first and removed only after the copy is verified**.
- **Delete account** for accounts (two taps): removes the account and its save.

The character name comes from the account (guests: the nickname). Saves are completely separate per account.

## 5. If browser storage is blocked
Register and Login explain that they can't work. **Guest still plays**, but nothing is saved.

## 6. When a real server arrives
1. Move accounts, password hashing (use Argon2id or bcrypt on the server) and sessions to the server. The browser must never decide who owns a save.
2. Saves live on the server, validated there (EXP, items and currency are decided server-side; see `REO-INSTRUCTIONS.md` rule on server authority).
3. Add: password reset by email, email verification, change password, rate limiting by IP, session expiry and "log out everywhere".
4. Offer an **import** of the local account and save the first time a player logs in, then delete the local copy.
5. Keep Guest as a temporary account that can be upgraded.

## 7. Open questions
1. Email at registration (needed for password reset)?
2. Should one account hold several characters (the character page already reserves 2 locked slots)?
3. Social login (Google, LINE, Apple)?
4. Terms of service and privacy notice text.
