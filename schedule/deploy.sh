RED='\033[0;31m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m' #NoColor
ENV=$1
SERVER_ENV=$ENV

if [ $# -eq 0 ]; then
    printf "${RED}You must pass environment as an argument${NC}. The options are:\n"
    printf "production\n"
    printf "demo\n"
    printf "test :( \n"
    exit 1
fi

printf "Preparing for release to ${BLUE}$ENV${NC} environment\n"
printf "Cleaning previous changes...\n"

git checkout .

if [ "$ENV" = "production" ] || [ "$ENV" = "demo" ]; then
  git checkout master
fi

if [ "$ENV" = "test" ] ; then
  git checkout integration
fi

printf "${GREEN}Fetching source code from GitHub${NC}\n"
git pull
GIT_EXIT_CODE=$?

if [ $GIT_EXIT_CODE -eq 1 ]; then
    printf "${RED}Error connecting to github, please check credentials! :( ${NC}\n"
    exit 1
fi


printf "${GREEN}Installing new packages provider schedule...${NC}\n"
npm install

NODE_ENV=$SERVER_ENV pm2 reload ecosystem.config.js

pm2 save

printf "${GREEN}Release done :)${NC}\n"
