# Check if 'new_folder' exists
if (Test-Path -Path "./new_folder") {
    # Create 'if_folder' if it doesn't exist
    if (-not (Test-Path -Path "./if_folder")) {
        New-Item -ItemType Directory -Path "./if_folder"
    }
}

# Check if 'if_folder' exists
if (Test-Path -Path "./if_folder") {
    # Create 'hyperionDev' if it doesn't exist
    if (-not (Test-Path -Path "./hyperionDev")) {
        New-Item -ItemType Directory -Path "./hyperionDev"
    }
}
else {
    # Create 'new-projects' if it doesn't exist
    if (-not (Test-Path -Path "./new-projects")) {
        New-Item -ItemType Directory -Path "./new-projects"
    }
}