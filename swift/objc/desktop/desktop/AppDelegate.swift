//
//  AppDelegate.swift
//  desktop
//
//  Created by Mars Liu on 15/3/2.
//  Copyright (c) 2015年 Dwarf Artisan. All rights reserved.
//

import Cocoa

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {



    func applicationDidFinishLaunching(aNotification: NSNotification) {
        // Insert code here to initialize your application
        NSLog("Hello, Mars Liu".sha1())
    }

    func applicationWillTerminate(aNotification: NSNotification) {
        // Insert code here to tear down your application
    }


}

