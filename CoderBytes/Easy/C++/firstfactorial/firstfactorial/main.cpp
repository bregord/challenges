//
//  main.cpp
//  firstfactorial
//
//  Created by Brendan on 2014-05-08.
//  Copyright (c) 2014 brendan. All rights reserved.
//


#include <iostream>

int firstFactorial(int num){
    
    if (num <=1 ) {
        return 1;
    }
    
    else{
        return num*firstFactorial(num-1);
    }
}

int main(int argc, const char * argv[])
{

    std::cout << "Insert number: ";
    int num;
    std::cin >> num;
    
    std::cout << "The factorial of " << num << " is " << firstFactorial(num) << std::endl;
    return 0;
}

 