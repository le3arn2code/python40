# Troubleshooting – Lab 1

## Issue 1: apt lock error
**Error:** Could not get lock /var/lib/dpkg/lock-frontend  
**Fix:**
```bash
sudo kill -9 <PID>
sudo rm -f /var/lib/dpkg/lock-frontend /var/lib/dpkg/lock /var/cache/apt/archives/lock
sudo dpkg --configure -a
sudo apt update
```

## Issue 2: Puppet GPG Key Expired
**Error:** EXPKEYSIG Puppet release key expired  
**Fix:**
```bash
sudo rm /etc/apt/sources.list.d/puppet*.list
sudo apt update
```

## Issue 3: Software mismatch
**Error:** Broken dpkg state  
**Fix:**
```bash
sudo dpkg --configure -a
sudo apt --fix-broken install
```
