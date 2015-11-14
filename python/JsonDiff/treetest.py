from treestruct import Node
from treedt import jstree_distance

A = (
    Node("start")
        .addkid(Node("meta")
            .addkid(Node("category"))
                .addkid(Node("plain"))
            .addkid(Node("catelog")   
                .addkid(Node("type"))))
        .addkid(Node("content"))
            .addkid(Node("this is jsontree-A"))
    )
B = (
    Node("start")
        .addkid(Node("meta")
            .addkid(Node("category"))
                .addkid(Node("message"))
            .addkid(Node("catelog")   
                .addkid(Node("type"))))
        .addkid(Node("content"))
            .addkid(Node("this is test"))
    )
assert jstree_distance(A, B)==2



C = (
    Node("start")
        .addkid(Node("meta")
            .addkid(Node("category"))
                .addkid(Node("plain"))
            .addkid(Node("catelog")   
                .addkid(Node("type"))))
        .addkid(Node("content"))
            .addkid(Node("meta"))
                .addkid(Node("category"))
                    .addkid(Node("plain"))
                .addkid(Node("content")   
                    .addkid(Node("this is jsontree-A")))
    )
                 
D = (
    Node("start")
        .addkid(Node("meta")
            .addkid(Node("category"))
                .addkid(Node("message"))
            .addkid(Node("catelog")   
                .addkid(Node("type"))))
        .addkid(Node("content"))
            .addkid(Node("this is jsontree-A"))
    )

assert jstree_distance(C,D)==5
