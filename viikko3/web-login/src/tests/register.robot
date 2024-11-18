*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Register Form
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Register Form
    Register Should Fail With Message  Username must consist of three or more characters

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Register Form
    Register Should Fail With Message  Password must consist of eight or more characters

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Submit Register Form
    Register Should Fail With Message  Password can't consist only of characters a-z

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  erisalasana
    Submit Register Form
    Register Should Fail With Message  Password and password confirmation differ

Register With Username That Is Already In Use
    Set Username  oleva
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Register Form
    Register Should Fail With Message  Username is already taken

Login After Succesful Registration
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Register Form
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Go To Login Page
    Set Username  kalle
    Set Password  kalle1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  short
    Set Password Confirmation  short
    Submit Register Form
    Register Should Fail With Message  Password must consist of eight or more characters
    Go To Login Page
    Set Username  kalle
    Set Password  short
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Register Form
    Click Button  Register

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  oleva  oleva123
    Go To Register Page