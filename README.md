<h1 style="text-align: center;">Welcome to The Recipe Book</h1>

The ultimate hub for food lovers and home cooks! Discover a world of delicious possibilities as you swap recipes with fellow cooking enthusiasts, rate and discuss your favourite dishes, and create a personalised collection of recipes you love. Whether you're mastering the art of cooking or just exploring new flavours, The Recipe Book brings a vibrant community of foodies right to your kitchen. Let’s cook, share, and savour together.

<img src="ReadMe/Images/recipebook.png" alt="Responsive images" style="width:500px;"/>

# Table of Contents

1. [Problem Statement](#problem-statement)
2. [Purpose](#purpose)
3. [Target Audience](#target-audience)
4. [Features](#features)
5. [Additional Features](#additional-features)
6. [Database Structure](#database-structure)
7. [User Experience / Wireframes](#userexperience-wireframes)
8. [Agile Methodology](#agile-methodology)
9. [User Stories](#user-stories)
10. [Testing](#testing)
11. [Deployment](#deployment)
12. [Citation of Sources](#citation-of-sources)
13. [Credits](#credits)


## Problem Statement
The most common question asked in my household is, "What's for dinner?" 
As a single working mum, this question fills me with dread and takes up more time than I feel I have to decide, shopping for ingredients and then preparing the meal. Then throw in a curve ball, a friend who has a gluten intolerance or allergy... pure panic! Which Is why I developed this recipe blog. A place to share and find recipes to help reduce the mealtime dread. 

## Purpose

Households are becoming busier and with the current climate the importance of meal planning to help tighter budgets is even greater. The purpose of this site is to help users to meal plan, budget and share great recipes.

## Target Audience

All those who cook our of enjoyment or necessity.

## Features

A login/Logout feature.
Comment section for users to add comments.
A page to upload and share recipes.
Recipes with ingredients timings and tags to any allergens.
Picture upload feature.
Links to social media to share recipes users have tried.

## Additional Features

A search bar to easily find a recipe
A filter to help reduce the number of recipes available/ remove those recipes that have certain ingredient in them.
A space for individuals to keep a recipe folder of there favourite recipes.

## Database Structure

<p align="center">
<img src="ReadMe/Images/EDR.png" alt="edr diagram" style="width:500px;"/>
</p>

## User Experience / Wireframes

<h2 style="text-align: center;">Mood Board that inspired the website.</h2>
<p align="center">The colour scheme was inspired by the rich vibrant colours of the herbs and spices used by many in their cooking.</p>

<p align="center">
<img src="ReadMe/Images/Moodboard.png" alt="mood board" style="width:500px;"/>
</p>
<h2 style="text-align: center;">Wire Frames</h2>
<p align="center">
<img src="ReadMe/Images/Desktop_Laptop Wireframe.png" alt="wireframe for desktop or laptop" style="width:200px; hight:100px"/> <img src="ReadMe/Images/Tablet.png" alt="wireframe for tablet" style="width:200px;"/> 
<br>
<img src="ReadMe/Images/Mobile Wireframe.png" alt="wireframe for mobile" style="width:100px;"/>
</p>

<h2 style="text-align: center;">Screen shots</h2>
<p align="center">

## Agile Methodology

<h3>Kanban Board</h3>
<p align="center">
<img src="ReadMe/Images/Kanban board.png" alt="wireframe for mobile" style="width:300px;"/>
</p>

<h3>Project Board</h3>
The project board can be found <a href="https://miro.com/app/board/uXjVLBAyMvE=/>">here</a>


## User Stories

| User Story | Feature |
| ----------| -------- |
| I am a user I want to be able to see the recipes clearly and be able to identify the ingredients needed | Recipe Cards with Ingredients |  
| I am a user I want to be have clear space to see and sort recipes| A space for users to store a collection of recipes |
|I am a user I want to be able to share my own recipes for others to use| Ability to upload users own recipes|
| As a user I want to be able to comment on recipes because I want to give feedback to others on how a recipe turned out. | Comment section under the recipe |
| As a user I want to be able to rate recipes and see which are the best to try myself | A star rating feature for each recipe |
|As an admin and I want to be able to monitor who is making comments on the recipes | Login feature with username |
| As a user I want to connect to my social media to share the recipes I have created| Social Media linked to the website |
| I am a user and I want to be able to log in so I can comment, rate and store my favourite recipes| Sign up feature |
| As a user I want to be able to sort recipes by ingredients because I can exclude any that may have allergens or ingredients I dislike.| Filter function for recipes|
| As a user I wish to upload photos of food I have created because I want feedback from others.| Photo uploading feature|
| As a user I want to be able to search for recipes of ingredients easily | Search function |

<h3>MoSCoW score features</h3>
Must Haves
<ul>
<li>Recipe Cards with Ingredients</li>
<li>A star rating feature for each recipe</li>
<li>login feature with username</li>
<li>Sign up feature</li>
<lil>Comment section under the recipe</li>
<li>Upload users own recipes</li>
</ul> 
Should Haves
<ul>
<li>Photo uploading</li>
<li>Social Media linked to the website</li>
</ul>
Could Haves
<ul>
<li>A space for users to store a collection of recipes</li>
<li>Search function</li>
</ul>
Won't Haves 
<ul>
<li>The ability to select ingredients and add to a shopping list.</li>
<li>Sort recipes and exclude those with allergens </li>
</ul>

## Testing
HTML and CSS validation performed by https://validator.w3.org/
<img src="/workspace/Recipe-Blog/ReadMe/Images/css.png" alt ="css errors screengrab">

<img src="ReadMe/Images/error1.png" alt ="html errors screengrab">

3 syntax errors noted and changed.

Python code put through CI Python Linter
all syntax errors adjust apart from 4 line indentation errors that I have left for readability. 

The current iteration fails on its accessibility due to low contrast between the orange font and the cream background. In a future iteration this should be looked at and changed accordingly.

<h3>Manual Testing</h3>

| Testing | Pass/Fail |
| ------- | --------- |
| Navigation | Pass - Can easily navigate between pages |
| Login/Logout feature | Pass - Login page & username on show when logged in |
| Comment Section | Pass - Users can add comments to recipes |
| Delete/Edit own comments | Pass - Users can edit or delete their own comments |
| Recipe Card | Pass - Multiple recipe cards can been seen at once |
| Clear and concise instructions | Fail - See below |
| Pictures can be uploaded along with recipes | Pass - Pictures can be uploaded by user or admin |
| Sign up feature for users | Pass - Users can sign up, however the CSS is currently not working |


<h3>Future Improvements</h3>
<ul>
<li>The units for the ingredients on the recipe cards are not very clear. In a future iteration I will look at adding more options to the ingredient model as well as having a blank option for users to customise.</li>
<li>When users upload recipes they are not uploading to the site after approval, they are being sent to admin to upload. This will be updated for a future iteration to allow the user to upload this once approved by admin.</li>
<li>The accessibility fails for this website due to the contrast between the orange text and the cream background. This should be looked at in a future iteration.</li>
<lil>The CSS needs to be addressed for the signup page.
</ul>

## Deployment

Heroku live link can be found [here](https://capstone-recipe-blog-a88392fc4fea.herokuapp.com/)




## Citation of Sources

| Description | Source |
| ----------- | ------ |
| Recipe content | Chat GPT |
| Stock Image of Cupcake  | https://www.pexels.com/photo/person-holding-cupcake-with-white-icing-4099127/ | 
| Stock Image of spices | https://www.pexels.com/photo/assorted-cooking-spices-2802527/ |
| Stock Image of bowl | https://www.pexels.com/photo/person-pouring-salt-in-bowl-11
|Stock Image of recipe book | https://www.pexels.com/photo/white-and-gray-chevron-print-recipes-book-833109/|
|Logo Design | Designed using Canva |
| Fonts | Google Fonts |
