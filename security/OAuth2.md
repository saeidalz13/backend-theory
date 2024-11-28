# OAuth2 and OpenID

## Terminology

- Resource owner -> you and me
- Client -> application (Yelp)
- Authorization Server -> System I can use to say yes (account.google.com)
- Resource Server -> google contacts API (or calendar or...)
- Authorization grant -> proves that the user clicked yes for granting access
- Redirect URI ->
- Access Token -> **THIS IS WHAT THE CLIENT WANTS**

## Flow

1. Us (resource owner) click on "Sign in with Gmail" through app (Client)
2. This redirects us to the "authorization server"

   - with this request, the app sends
     - Redirect URI: yelp.com/callback
     - Response type: code (the most common)
     - Scope: profile contacts

3. If everything went successful
   - the auth server redirects to the requested redirect URI
   - along with authorization code
4. We can't do a lot with that aut code.
   - What we can do with it is to **exchange authorization code with access token**
   - if ok -> auth server says to the client: Ok! here is your access token
5. Now the client can contact the resource server (calendar or photos or ...) with access token
   - Most likely limited access (Read-Only)

And that's it!

## More Terminology

- Scope (read/write/delete/...)
- Consent


## A little more terminology

- Back channel (highly secure) -> our own server
- Front channel (less secure) -> browser

That's why authorization code is sent to the redirect URI (with front channel). 
Then the exchange for access token happens through server and not browser (with back channel).

## How does this actually happen

1. When the button (sign in with google) is clicked, the GET request goes to:
    - https://accounts.google.com/o/oauth2/v2/auth?
        - client_id=
        - redirect_id=
        - scope=
        - response_type=
        - state=

So I create a client on google account (dev)
I get:
    - client_id
    - client_secret
These identify me to the authorization server.


