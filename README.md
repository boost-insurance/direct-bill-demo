# direct bill demo

This is the demo repo for Boost's Direct Bill feature. 

### Requirements

We support python 3.8.

### Setup

Install requirements in a virtualenv.

```bash
pip install -r requirements.txt
```

Fill out `.env` file.

Environment variable | Description
---|---
`BOOST_API_URL` | Defaulted to the sandbox URL, recommended to only use this demo in sandbox.
`BOOST_API_AUTHORIZATION_TOKEN` | "access_token" returned by `POST /auth/oauth2/token`.
`BOOST_USER_HEADER` | Value used for BOOST-USER header, we will provide this.
`STRIPE_PUBLISHABLE_KEY` | Publishable Stripe key, used to render Stripe elements and create Stripe PaymentMethods, we will provide this. Note that this is a different key for sandbox and production.

Start SSL server.

```bash
python manage.py runsslserver
```

Go to `https://localhost:8000/` and you should see the Checkout form.

### Usage

* Create a quote (`POST /quotes`), copy the UUID
* Use the UUID in the Checkout form
* Use one of Stripe's Test Cards [(docs)](https://stripe.com/docs/testing)
