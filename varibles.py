//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VariableExamples {
    uint public age = 25;
    int public temperature = -5;
    uint8 public smallnum = 255;

    string public name = "alice";
    bool public isActive = true;
    address public owner;

    function calculate() public pure returns (uint) {
        uint temp = 10;
        uint result = temp * 2;
        return result;
    }

    function productAndAverage() public pure returns (uint product, uint average) {
        uint a = 4;
        uint b = 6;
        uint c = 8;

        product = a * b * c;

        average = product/ 3;
    }
}