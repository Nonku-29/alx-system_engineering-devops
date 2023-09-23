#!/usr/bin/python3
"""Script that, using the GitHub REST API, for a given user,
   returns information about his/her repositories."""
import requests
from sys import argv

if __name__ == '__main__':
    # Get the user response
    appEndpoint = 'https://api.github.com'
    userResponse = requests.get(appEndpoint + '/users/' + argv[1] + '/repos').json()

    # Get repository names and descriptions
    repoNames = [repo['name'] for repo in userResponse]
    repoDescriptions = [repo['description'] for repo in userResponse]

    print('The user {} has the following repositories:'.format(argv[1]))

    for i in range(len(repoNames)):
        print('{}. {}'.format(i+1, repoNames[i]))
        print('\t{}'.format(repoDescriptions[i] if repoDescriptions[i] else 'No description provided.'))
