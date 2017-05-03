'use strict';

var accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an balance of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - balance
//
// Log "404 - account not found" if any of the account numbers don't exist to the console.

function bankInfo(account) {
    return 'Account Name: ' + account.client_name + '\n' + 'Balance: ' + account.balance + '\n'
}

// console.log(bankInfo(accounts[1]))

////////////////////////////////////////////////////////////////////////

function bankTransfer(from, to, sendMoney) {
    var validAccountNubers = [accounts[0].account_number, accounts[1].account_number, accounts[2].account_number]

    if (validAccountNubers.includes(from) && validAccountNubers.includes(to)){
        for (var i = 0; i <= validAccountNubers.length; i++) {
            if (accounts[i].client_name == from.client_name) {
                accounts[i].balance -= sendMoney;
            } else if (accounts[i].client_name == to.client_name) {
                accounts[i].balance += sendMoney;
            }
        }
    }else {
        return 'Invalid usernames'
    }
}

console.log(bankInfo(accounts[1]), bankInfo(accounts[2]))
bankTransfer(43546731, 23456311, 1000000000)
console.log(bankInfo(accounts[1]), bankInfo(accounts[2]))
