# PitchPitches

> A pitching website for pitching quotes and ispirations

## Author

> By **Manasseh Bundi**

> -----------------------------------------------------------

## Description

> This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (General, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

## User Stories

As a user I would like:

> * to vsee the pitches other people have posted
> * to vote on the pitch they liked and give it a downvote or upvote
> * to be signed in for me to leave a comment
> * to receive a welcoming email once I sign up.
> * to view the pitches I have created in my profile page
> * to comment on the different pitches and leave feedback
> * to ubmit a pitch in any category.

## How to use it

> * Internet connection
> * Click ) <br/>
  

## How it works

> * A user can sign up

> * A user can also post comments and articles.

## Technologies Used

> * Python3.6
> * Flask framework
> * Bootstrap and Css
> * PostgreSQL
> * SQLAlchemy

## Setup/Installation Requirements

### Prerequisites

> * Internet access
> * ```git clone ```
> * ```cd pitchpitches```

#### To install a virtual environment

> * ```python3.6 -m venv virtual``` 
> * ```source virtual/bin/activate```

#### To install all dependencies

> * ```python3.6 -m pip install -r requirements.txt```

#### To change the config_name parameter from 'production' to 'development'

> * Inside the manage.py module  i.e:- ```app = create_app('production')``` should be ```app = create_app('development')```
> * Then run ```python3.6 manage.py server``` to get the app running  navigate to ```http://127.0.0.1:5000/``` and it will open in your browser

## Dependancy Installments

> * pip install python3.6
> * pip install flask
> * pip install flask-bootstrap
> * pip install flask-script
> * pip install flask-wtf
> * pip install flask-migrate
> * pip install flask-login
> * pip install Flask-Mail
> * pip install flask-uploads

## Specifications

> * To see the projects specifications refer to the [SPECS.md](SPECS.md) file for more details.



## Support and Contact Details

> You can reach out to me at manassehbundi2017@gmail.com
for Reviews, Advice, Collaborations and Comments

## Licence

> MIT License

> Copyright (c) 2020 **Manasseh Bundi**

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

> --------------------------------------------------------