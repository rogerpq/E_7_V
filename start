#!/bin/bash


_get_ziplink () {
    local regex
    regex='(https?)://github.com/.+/.+'
    if [[ $UPSTREAM_REPO == "Rep" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL1JlcHRob25BcmFiaWMvUmVwdGhvbkFyL2FyY2hpdmUva295ZWIuemlw" | base64 -d
    elif [[ $UPSTREAM_REPO =~ $regex ]]
    then
        if [[ $UPSTREAM_REPO_BRANCH ]]
        then
            echo "${UPSTREAM_REPO}/archive/${UPSTREAM_REPO_BRANCH}.zip"
        else
            echo "${UPSTREAM_REPO}/archive/koyeb.zip"
        fi
    else
        echo "aHR0cHM6Ly9naXRodWIuY29tL1JlcHRob25BcmFiaWMvUmVwdGhvbkFyL2FyY2hpdmUva295ZWIuemlw" | base64 -d
    fi
}

_get_repolink () {
    local regex
    local rlink
    regex='(https?)://github.com/.+/.+'
    if [[ $UPSTREAM_REPO == "Rep" ]]
    then
        rlink=`echo "aHR0cHM6Ly9naXRodWIuY29tL1JlcHRob25BcmFiaWMvUmVwdGhvbkFyLmdpdA==" | base64 -d`
    elif [[ $UPSTREAM_REPO =~ $regex ]]
    then
        rlink=`echo "${UPSTREAM_REPO}"`
    else
        rlink=`echo "aHR0cHM6Ly9naXRodWIuY29tL1JlcHRob25BcmFiaWMvUmVwdGhvbkFyLmdpdA==" | base64 -d`
    fi
    echo "$rlink"
}


_run_python_code() {
    python3${pVer%.*} -c "$1"
}

_run_catpack_git() {
    $(_run_python_code 'from git import Repo
import sys
OFFICIAL_UPSTREAM_REPO = "https://github.com/RepthonArabic/RepthonAr"
ACTIVE_BRANCH_NAME = "koyeb"
repo = Repo.init()
origin = repo.create_remote("temponame", OFFICIAL_UPSTREAM_REPO)
origin.fetch()
repo.create_head(ACTIVE_BRANCH_NAME, origin.refs[ACTIVE_BRANCH_NAME])
repo.heads[ACTIVE_BRANCH_NAME].checkout(True) ')
}

_run_cat_git() {
    local repolink=$(_get_repolink)
    $(_run_python_code 'from git import Repo
import sys
OFFICIAL_UPSTREAM_REPO="'$repolink'"
ACTIVE_BRANCH_NAME = "'$UPSTREAM_REPO_BRANCH'" or "koyeb"
repo = Repo.init()
origin = repo.create_remote("temponame", OFFICIAL_UPSTREAM_REPO)
origin.fetch()
repo.create_head(ACTIVE_BRANCH_NAME, origin.refs[ACTIVE_BRANCH_NAME])
repo.heads[ACTIVE_BRANCH_NAME].checkout(True) ')
}

_set_bot () {
    local zippath
    zippath="RepthonAr.zip"
    echo "جاري تنزيل اكواد السورس "
    wget -q $(_get_ziplink) -O "$zippath"
    echo " تفريغ البيانات "
    CATPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo " تم التفريغ "
    echo " يتم التنظيف "
    rm -rf "$zippath"
    sleep 5
    _run_catpack_git
    cd $CATPATH
    _run_cat_git
    python3 ../setup/updater.py ../requirements.txt requirements.txt
    chmod -R 755 bin
    echo "   جـار بـدء تـنزيـل ريبـــثون   "
    echo "

    "
    python3 -m zthon
}

_set_bot
