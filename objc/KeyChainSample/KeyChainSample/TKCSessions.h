//
//  TKCSessions.h
//  KeyChainSample
//
//  Created by Mars Liu on 13-11-27.
//  Copyright (c) 2013年 Traveltao. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface TKCSessions : NSObject

@property (readonly) NSString *token;
@property (readonly) NSString *refreshToken;
@property (readonly) NSString *user;

@end
