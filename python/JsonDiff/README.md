test simple:
===================================  
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
