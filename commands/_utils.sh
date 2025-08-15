#!/bin/bash

print_error() {
    local msg="$1"
    echo -e "\e[31m[ERROR] $msg\e[0m"
}

print_operation() {
    local msg="$1"
    echo -e "\e[94m$msg\e[0m"
    echo ""
}

print_info() {
    local section="$1"
    local msg="$2"
    echo -e "\e[96m$section\e[0m: $msg"
}

print_warning() {
    local msg="$1"
    echo -e "\e[93m[WARNING] $msg\e[0m"
}

print_start() {
    echo ""
    echo -e "\e[92mStarting...\e[0m"
}

print_text() {
    local msg="$1"
    echo -e "\e[97m$msg\e[0m"
}

print_end() {
    echo ""
    echo -e "\e[92mDone.\e[0m"
}

print_invalid_argument() {
    print_error "Error: Invalid argument"
    print_text ""
    print_usage
}
