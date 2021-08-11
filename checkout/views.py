import json

import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index_view(request):
    """
    Renders the Boost Direct Bill Demo homepage.
    """
    return render(
        request,
        "checkout/index.html",
        {"stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY},
    )


class CheckoutView(View):
    def post(self, request):
        """
        Wrapper for Boost endpoint to pay for policies (POST /policy-payments).
        """
        data = json.loads(request.body)

        request_headers = {
            "Content-Type": "application/vnd.api+json",
            "boost-user": settings.BOOST_USER_HEADER,
            "Authorization": f"Bearer {settings.BOOST_API_AUTHORIZATION_TOKEN}",
        }
        request_body = {
            "data": {
                "type": "policy_payment",
                "attributes": {"stripe_payment_method_id": data["paymentMethodId"]},
                "relationships": {
                    "quote": {"data": {"type": "quote", "id": data["quoteId"]}}
                },
            }
        }

        try:
            response = requests.post(
                f"{settings.BOOST_API_URL}/policy-payments",
                data=json.dumps(request_body),
                headers=request_headers,
            )
        except Exception as e:
            print(e)

        return HttpResponse(
            json.dumps(response.json(), indent=4), status=response.status_code
        )
