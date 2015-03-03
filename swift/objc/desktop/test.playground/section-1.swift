// Playground - noun: a place where people can play

import Cocoa

var str = "Hello, playground"

// CommonCrypto 构造
// 这里的字符串 Hash 算法使用了 libcommonCrypto 库，这是一个 C 库，内部使用 OpenSSL 实现。
// 要在 swift 项目的编译环境中使用  libcommonCrypto ，可以用 Brigding Header 。

import CommonCrypto

extension String {
    func sha1() -> String {
        let data = self.dataUsingEncoding(NSUTF8StringEncoding)!
        var digest = [UInt8](count:Int(CC_SHA1_DIGEST_LENGTH), repeatedValue: 0)
        CC_SHA1(data.bytes, CC_LONG(data.length), &digest)
        let output = NSMutableString(capacity: Int(CC_SHA1_DIGEST_LENGTH))
        for byte in digest {
            output.appendFormat("%02x", byte)
        }
        return output
    }
}

var ret = str.sha1()

