from datetime import datetime

# TODO: This should be a database call or something similar
context_variables = {
    "customer_context": {
        "CUSTOMER_ID": "customer_12345",
        "NAME": "John Doe",
        "PHONE_NUMBER": "(123) 456-7890",
        "EMAIL": "johndoe@example.com",
        "LEAD_TYPE": "l0",
    },
    "general_context": {"current_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
}
