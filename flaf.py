def A():
    import turtle as t
    d=t.Turtle()
    d.begin_fill();d.fillcolor("Orange")
    d.left(90);d.forward(40);d.right(90);d.forward(150);d.right(90);d.forward(40);d.right(90);d.forward(150);d.end_fill()

    d.begin_fill();d.fillcolor("white")
    d.left(90);d.forward(40);d.left(90);d.forward(75);d.begin_fill();d.fillcolor("white");

    d.circle(20);    
    d.left(90);d.forward(40);d.backward(20);d.right(90);d.forward(20);d.backward(40);d.forward(20);d.left(45);d.forward(20);d.backward(40);d.forward(20);
    d.right(90);d.forward(20);d.backward(40);d.forward(20);d.right(135);d.forward(20);d.backward(40);d.forward(20);d.end_fill();d.left(90);d.forward(20);d.left(90);d.forward(75);d.left(90);d.forward(40);d.backward(40)

    d.begin_fill();d.fillcolor("dark green")
    d.backward(40);d.left(90);d.forward(150);d.right(90);d.forward(40);d.end_fill()

    
A()
