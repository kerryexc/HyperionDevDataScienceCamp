# Step 1: Create three main folders
New-Item -ItemType Directory -Name "MainFolder1"
New-Item -ItemType Directory -Name "MainFolder2"
New-Item -ItemType Directory -Name "MainFolder3"

# Step 2: Navigate into one of the main folders (MainFolder1)
Set-Location -Path "MainFolder1"

# Step 3: Create three subfolders inside MainFolder1
New-Item -ItemType Directory -Name "SubFolderA"
New-Item -ItemType Directory -Name "SubFolderB"
New-Item -ItemType Directory -Name "SubFolderC"

# Step 4: Navigate back to the parent directory
Set-Location ..

# Step 5: Remove the other two main folders
Remove-Item -Recurse -Force "MainFolder2"
Remove-Item -Recurse -Force "MainFolder3"