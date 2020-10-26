# Gregslist
Your goal: Build a second-hand message-board website!

Don't worry, you don't need to knock it out in one punch, there are several
iteretions to this exercise:

## Step 1 - Item Messages
Build URLs to post and get messages. At this stage the board is anonymous -
there are no accounts!

## Step 2 - Update/Delete
Add update and delete views. To authorize those actions, generate a passcode
in the creation phase. The passcode will be validated on update/delete
requests.

* Passcode should be returned in the response to new item posts.
* Do not redirect, think about the security implications.

## Step 3 - feed
Add URL that returns the messages feed, pagable by number of messages, and
filterable by given message title.

## Step 4 - Accounts
Add user accounts. This includes register/login/logout URLs. Login/logout
should operate a session cookie.

* Accountless posting (via passcode) should still work.
* New posts by authenticated users can skip the passcode in the response
* Passcode fields should be hidden for authenticated users.

## Step 5 - I18N
Your board goes international (Don't worry, shippings are out of scope, for
now).

Add a currency field to your account models, with a handful types available.
Now, every price displayed on the board should be translate to the user's
preferred currency. Currency values are to be updated from a 3rd party service
called [OpenRates](https://openrates.io/).

conversions against the service should be cached for 30 minutes, as quering it
for each request will bring the service down (or at least cause them to block
you).

You should have a fallback value available locally in case the service cannot
be reached.

## Exercise completion marker
This exercise has no automated tests! as a result, you need to
acknoledge you finished the tasks yourself. do it by creating
a file named `DONE` in this directory.
