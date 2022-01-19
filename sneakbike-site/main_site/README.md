# Sneakbike Site

This is the code for `sneak.bike`, primarily in Vue.js.

---

# I want to contribute, but I'm scared.

Okay, don't be scared.

## Step 1: Stuff You'll Need

I'm assuming you're on Windows here; if you're on another OS, the instructions will be similar.  Here's what you'll need:

- A [github](https://github.com/) account.
  - This will be useful for you to have for all your future coding adventures and potentially useful as a portfolio for future coding jobs, so choose a name that's appropriate.
- [Github for Windows](https://desktop.github.com/).
  - You can also use `choco install git` if you use chocolatey, or whatever other github management tool you'd like.
- [Nodejs](https://nodejs.org/en/download/).
  - Click on the "Windows" download, then install.
- A nice text editor.  We strongly recommend [Visual Studio Code](https://code.visualstudio.com/) if you don't have a favorite yet.

Great, now you have everything you'll need.

## Step 2: Running the Site Locally

We're going to do the following things: **clone the sneakbike repo, run the API in the background, then serve the site locally.**  You'll be able to make changes to the API or the Site and see these changes without pushing them to production!  Neat.

1. Read the first few steps [here](https://docs.github.com/en/free-pro-team@latest/desktop/installing-and-configuring-github-desktop/getting-started-with-github-desktop) at the github for windows site.  It'll show you how to open, authenticate, and clone a repository.  
   - You'll only need to read up to "Creating, adding, and cloning repositories." for what we need.
2. Clone the Sneakbike repository by using the URL: `https://github.com/jsal13/sneakbike-site.git`
3. Open CMD or Powershell and navigate to the Sneakbike Directory.
   - For example, if the Sneakbike directory is at `C:\Users\yourname\Documents\sneakbike-site` then you can type 
   > `cd ~/Documents/sneakbike-site`  
  
   - The `~` is a shorthand for `C:\Users\yourname` and the `cd` means "change directory".
4. Go into the "main_site" folder and Run 
   > `npm i`
5. Once this is done, in the same folder, run 
   > `npm run serve`
6. Go to a browser (Chome, Firefox, etc.) and go to the url
   > `localhost:8080`

You should see the Sneakbike website!  This is all local, meaning only you can see it, but this means you can modify the code to your heart's content before we push it to production.

## Step 3. Making Changes

You make the changes you want.  If you're not sure where to go, ask someone in the Sneakbike discord or open an issue here!

## Step 4. Pushing Your Changes

Alright, you've made changes.  Now you need to push these changes up to github and have someone review them and merge them into the production code if everything looks good.

[This document](https://docs.github.com/en/free-pro-team@latest/desktop/contributing-and-collaborating-using-github-desktop/committing-and-reviewing-changes-to-your-project) shows the steps necessary to do this.  Loosely, it's like this:

1. Make a branch,
2. Add files you wanna push up (it'll show the changed ones),
3. Title your "commit" something like, "chore: changed names for bingo".
4. Push to the branch.

Once you do this, you go to [the Sneakbike Github](https://github.com/jsal13/sneakbike), click on the "`Pull Requests`" tab, then the `New Pull Request` button.  Pick your branch and open up a PR.  You can let someone know on the team that you've done so, and they will review your code and either give comments or approve it and merge it.

At this point, your new code will be in the app whenever it is rebuilt (usually weekly, sometimes more often).