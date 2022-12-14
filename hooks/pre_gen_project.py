#!/usr/bin/env python

import logging
import subprocess

LOGGER = logging.getLogger(__name__)

################################################################################
# Check that source_directory and test_directory are distinct
################################################################################

source_directory = "{{cookiecutter.source_directory}}"
test_directory = "{{cookiecutter.test_directory}}"

if source_directory == test_directory:
    LOGGER.error(
        f"ERROR: 'source_directory' and 'test_directory' cannot be the same directory: {source_directory}"
    )
    exit(1)

################################################################################
# Print GHC and cabal versions
################################################################################

ghc_version = "{{cookiecutter.__ghc_version}}"

LOGGER.info(f"Using GHC version {ghc_version}")

cabal_version = "{{cookiecutter.__cabal_version}}"

LOGGER.info(f"Using Cabal version {ghc_version}")

################################################################################
# Check that fullname and email match git config
################################################################################

try:
    fullname = "{{cookiecutter.fullname}}"
    git_fullname = subprocess.getoutput("git config --get user.name")
    if fullname != git_fullname:
        LOGGER.warn(f"'{fullname}' does not match git config: '{git_fullname}'")
except subprocess.CalledProcessError as e:
    LOGGER.warn(f"Could not check git config: {e}")

try:
    email = "{{cookiecutter.email}}"
    git_email = subprocess.getoutput("git config --get user.email")
    if email != git_email:
        LOGGER.warn(f"'{email}' does not match git config: '{git_email}'")
except subprocess.CalledProcessError as e:
    LOGGER.warn(f"Could not check git config: {e}")
