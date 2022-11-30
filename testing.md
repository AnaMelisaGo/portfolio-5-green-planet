# Testing

## Table of contents

1. [Code validation](#code-validation)
    - [HTML](#html)
2. [Found bugs](#found-bugs-and-fixes)

---

## Code validation

Testing was carried out with the following validators:

   - W3C Markup and CSS Validator - No errors were found in the code.

   - JSHint Validator - No errors were found in the code.

   - PEP8 CI Validator - No errors were found in the code.

All validity tests passed. Most of the error in CSS Validator is due to Bootstrap and mailchimps webkits.



### HTML

| Page | Result |
| ---- | ------ |
| Home | No error |
| Store | No error |
| Add Store | No error |
| Edit Store | No error |
| For Businesses | No error |
| Account | No error |
| Add Business Type | No error |
| Edit Profile | No error |
| Favourite List | No error |
| Login | No error |
| Log out | No error |
| Sign In | No error |
| Bag | No error |
| Checkout user | No error |
| Checkout | No error |

[Back to top](#Table-of-contents)

---

## Found Bugs and Fixes:
 
During manual testing some minor and major bugs was encountered.

- Tested the app for the first time and it is running perfectly. No errors were found.

- When trying to push for the first time, an error showed up stating “Updates were rejected because the remote contains work that you do not have locally.” I managed to force push the initial commit by typing the command in the terminal `git push -f origin main`.

- When adding media content to the website, the images were not showing up properly. It appeared broken. I fixed it by adding a context processor for the media root in settings.py `django.template.context_processors.media`.

- Error in sorting the name and category name due to the naming convention was interfering with the split function in javascript. Sorting by name and category was fixed by adding an if statement in the code so that it matches the variable names in the models. Couldn’t fix the sorting style in the page due to the time limit. I could have added the `filter all` dropdown menu to the main nav.

- Initializing the toast wasn't easy. Bootstrap 5 was different and I needed some guides on how to get it working. I managed to make it work with the help of the tutors and this [Guide](https://stackoverflow.com/questions/63515279/how-to-initialize-toasts-with-javascript-in-bootstrap-5
).

- When testing the checkout form, it wasn’t working well. At first I put the names of the fields the wrong way. Bootstrap 4 template pack wasn’t working well so I needed to install crispy form bootstrap 5 [link](https://stackoverflow.com/questions/65238459/templatedoesnotexist-at-users-register-bootstrap5-uni-form-html)  using the command `pip3 install crispy form bootstrap 5` and adding it to installed apps in settings.py.

- FAvicon wasn’t working well. The error was that I added the favicon in the images folder and not in the static folder. Fix it by adding images folder inside static folder and move the favicon icon inside this folder.

- After much deliberation I added a new field in store models to provide the user the location of the business for collection. I also added this data to the checkout success page for the user.

- To be able to get the full name of the user without going to the admin area, I was able to add a user form using the user model. This form is then passed to the template for editing or updating the first name, last name and email address of the user.

- The phone number of the user is added as inline in the admin area for the superuser easy access, instead of registering separately. It is better for readability and easy access. Help from [here](https://www.youtube.com/watch?v=NLHmadrP8Y4).

.The checkout template is modified from its initial style. When testing to checkout with the new checkout template, the checkout_success wasn’t working properly and the loader was stuck. Using the transaction form in views.py wasn’t working well. I manage to fix the problem by getting the user profile if the user is authenticated and if not it redirects the user to the sign up page or login if the user already has an account.

- When testing to add more stores in the webpage, the toast success notification message keeps on showing up the bag contents when something is in the bag. I couldn’t find any solution to hide the bag contents during this process so I used message.info instead. It also happens to edit and delete views. Same solution was done.

- When trying to implement a customized ClearableFileInput, the template wasn’t rendering well. Thanks to a tutor (Joshua) we found out where the bug is. The crispy form was formatting the fields so the customize template wasn’t appearing. To fix this problem a for loop was done through the fields in edit_store template and those that are not image fields would be formatted using crispy forms and the image field would be left as {{ field }}. By doing this it will be applied perfectly when using the widget  in forms.py with the custom ClearbleFileInput in the image field.

- When trying to set up a modal for the delete button for business types, the modal wasn’t taking the id of the business type selected. It only gets the id of the first business type in the loop.

- When trying the new animation keyframes in signup form, the code wasn’t working, but in edit business type template. To fix it, display: flex should be on the parent container to make it work. I added the bootstrap d-flex class on the parent container when using these keyframes.

- Subscription form in the footer works perfectly. No errors. Receives the subscription request through mailchimp website.

- Had a major issue with the webhook handler during payment.intent in Stripe. Assistance was needed a couple of times to make it work. We found out that the code had major flaws in some variables and in some adjustment I performed at the last minute. I fixed those problems by redoing and reviewing the entire code. The attribute DoesNotExist was misspelled, json.loads() should have the trailing ‘s’ (not load) since they are two different functions with very similar names. `json.load()`  takes a file-like object with a read() method,` json.loads()` takes a string. Found this solution on stackoverflow [here](https://stackoverflow.com/questions/11174024/attributeerrorstr-object-has-no-attribute-read). After reviewing the code and making adjustments I managed to make the webhook handler to work and it is finally sending a confirmation email about the transaction.

- When testing the deployed project, the static files weren’t loading well. To fix it, I had to disable the cache in the devtools under network menu to make it work.

- When trying to get a screenshot of the deployed site for readme documentation through `iamresponsive` website, the project wasn’t showing well. The problem was the cross origin. To fix it, I added in settings.py this code: `X_FRAME_OPTIONS = ‘SAMEORIGIN’` . Then in the views.py of my homepage in `home` app I imported `from django.views.decorators.clickjacking import xframe_options_exempt` and on top of the view function I included `@xframe_options_exempt`. I committed changes and deployed to heroku and it worked.

- When testing the 404 error page, in production it wasn’t rendering well. The problem was DEBUG in settings.py was set to True. To fix it and view it in the deployed project for testing, I had to change `DEBUG = False` and it worked perfectly.
