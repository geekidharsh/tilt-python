# From a bunch of chocolates and a chilli in a jar.
# Find a way to pick any number of chocolates each time so that the last item left is always the chilli
# total number of items in the jar is given

def main():
	items = ['choco', 'choco', 'choco', 'choco','choco', 'choco', 'choco', 'choco', 'choco', 'choco', 'choco', 'choco', 'chilli']
	totalLeft = int(len(items))
	print totalLeft

	for x in totalLeft:
		chilliPicker(x)

def chilliPicker():
	print items

	# chocolates = items - 1
	# chilli = 1
	# count of turn

	# player1, player2

	## algorithm

	# 1. divide total item in groups of 4
	# 2. after every round, your pick is = 4 - look at what the opponent took.
	# 3. repeat
	# 4. print final result should be chilli


if __name__ == '__main__':
	main()

# Khan academy solution in javascript
# // 5/11/16 - Watched "The Secret Rules of Modern Living: Algorithms" on Netflix
# // the host demonstrated a game he would play with 13 candies and 1 hot chili
# // the 2 players would take turns taking 1/2/3 candies out of the jar
# // the player that is without candies to take has to eat the hot chili
# // the host knows the algorithm to win:
# // 13 divides into 4 groups of 4 with 1 remainder
# // so take 1 on the 1st turn, and take the difference after Player 2 to complete the set of 4
# // Player 1 would finish the last set, leaving Player 2 with the hot chili
# // 5/12/16 - visualizing this algorithm to find how to beat it as Player 2

# background(51);
# rectMode(CENTER);
# textAlign(CENTER, CENTER);
# angleMode = "radians";
# noStroke();

# var jar; // Jar object
# var num; // num of candies
# var candies = []; // array of Candy objects
# var player; // player Object
# var playerBool; // false = Player 1 (left), true = Player 2 (right)
# var mouseFlag; // so the mouseIsPressed occurs only ONCE
# var candySizeW; // define the width of the Candy Object
# var candySizeH; // define the height of the Candy Object

# var turnCount; // keeps track of candies taken per turn - MAX 3 / turn


# // in draw() so that there's a new array every draw()
# // var active = []; // to determine what Objects are active, highest z-index wins

# var Jar = function(x, y, w, h) {
#     // Jar
    
#     this.x = x;
#     this.y = y;
#     this.w = w;
#     this.h = h;
    
#     var delta = this.h > this.w ? (this.h/100) : (this.w/100);
    
#     this.show = function() {
#         stroke(0, 130, 124);
#         strokeWeight(2);
        
#         fill(0, 150, 150, 50); // opening
#         ellipse(this.x, this.y - (this.h/2), this.w, this.h/10);
        
#         fill(0, 255, 255, 15); // main
#         beginShape();
#         vertex(this.x - (this.w/2), this.y - (this.h/2));
#         for (var a = 180; a >= 90; a -= delta) {
#             var ePX = (this.x - (this.w/4)) + floor((this.w/4)  * (cos(radians(a))));
#             var ePY = (this.y + (this.h/3)) + floor((this.h/8) * (sin(radians(a))));
#             vertex(ePX, ePY);
#         }
#         for (var a= 90; a >= 0; a -= delta) {
#             var ePX = (this.x + (this.w/4)) + floor((this.w/4)  * (cos(radians(a))));
#             var ePY = (this.y + (this.h/3)) + floor((this.h/8) * (sin(radians(a))));
#             vertex(ePX, ePY);
#         }
#         for (var a = 0; a <= 180; a+= delta) {
#             var ePX = this.x + floor((this.w/2)  * (cos(radians(a))));
#             var ePY = (this.y - (this.h/2)) + floor((this.h/20) * (sin(radians(a))));
#             vertex(ePX, ePY);
#         }
#         endShape();
#     };
    
    
# };

# var Candy = function(x, y, w) {
#     this.x = x;
#     this.y = y;
#     this.w = w;
#     this.h = w/1.5;
#     this.visible = true; // visible if in Jar, INVISIBLE if NOT in Jar
#     this.colorOff = color(133, 126, 0);
#     this.colorOn = color(255, 0, 0);
#     this.highlight = false;
    
#     this.inRegion = function() {
#         var mx = mouseX;
#         var my = mouseY;
#         var h = this.x;
#         var k = this.y;
#         var rx = this.w/2;
#         var ry = this.h/2;
        
#         var result = ( ( (mx - h)*(mx - h) ) / (rx*rx) ) + ( ( (my - k)*(my - k) ) / (ry*ry) ) <= 1;
#         // println(result);
#         return result;
#     };
    
#     this.show = function(x, y) {
#         if (this.visible) {
#             if (this.highlight) {
#                 fill(this.colorOn);
#             }
#             else {
#                 fill(this.colorOff);
#             }
            
#             // if (mouseIsPressed && mouseFlag && this.inRegion()) {
#             //     if (!playerBool) {
#             //         this.x = 20;
#             //     }
#             //     else {
#             //         this.x = width - 20;
#             //     }
#             // }
            
#             stroke(0);
#             strokeWeight(1);
#             ellipse(this.x, this.y, this.w, this.h);
#         }
#     };
# };

# var Player = function() {
    
#     textSize(height*0.1);
#     this.turnW = textWidth("Player #'s turn!") * 1.1;
#     this.turnH = height*0.15;
#     this.turnX = width/2;
#     this.turnY = this.turnH/1.75;
#     this.turnTextW = textWidth("Player #'s turn!");
#     this.turnBg1 = color(64, 128, 66, 150);
#     this.turnBg2 = color(151, 189, 0, 150);
    
#     this.turn = function() {
#         var playerNum = !playerBool ? 1 : 2;
#         noStroke();
#         if (!playerBool) {
#             fill(this.turnBg1);
#         }
#         else {
#             fill(this.turnBg2);
#         }
#         rect(this.turnX, this.turnY, this.turnW, this.turnH);
        
#         fill(0);
#         textSize(height*0.1);
#         text("Player " + playerNum + "'s turn!", this.turnX, this.turnY);
#     };
    
#     textSize(height*0.1);
#     this.butW = textWidth("SWITCH PLAYER") * 1.15;
#     this.butH = height*0.15;
#     this.butX = width/2;
#     this.butY = height - (this.butH/1.75);
#     this.butBg = color(0, 0, 0, 100);
#     this.butHover = color(255, 0, 0);
#     this.butPressed = color(255, 255, 255);
#     this.butColor = this.butBg;
    
    
#     this.button = function() { // to switch between Player 1 (left) and Player 2 (right)
#         fill(this.butColor);
#         noStroke();
#         rect(this.butX, this.butY, this.butW, this.butH);
        
#         textSize(height*0.1);
#         fill(0);
#         text("SWITCH PLAYER", this.butX, this.butY);
        

#         var mx = mouseX;
#         var my = mouseY;
        
#         if (mx > this.butX - (this.butW/2) && mx < this.butX + (this.butW/2) && my > this.butY - (this.butH/2) && my < this.butY + (this.butH/2)) {
#             this.butColor = this.butHover;
#             if (mouseIsPressed) { // 
#                 this.butColor = this.butPressed;
#                 if (mouseFlag) {
#                     playerBool = !playerBool;
                    
#                     turnCount = 3; // NEW
                    
#                     // mouseFlag = false; // this here doesn't work right on K.A, see mousePressed() function 
#                 }
#             }
#         }
#         else {
#             this.butColor = this.butBg;
#         }
#     };
    
    
#     textSize(height * 0.08);
    
#     this.pile1array = [];
#     this.pile1x = width*0.15;
#     this.pile1textColor = color(128, 0, 153);
    
#     this.pile2array = [];
#     this.pile2x = width*0.85;
#     this.pile2textColor = color(189, 76, 0);
    
#     this.pileY = height*0.25;
#     this.pileTextW = textWidth("Player #")/2;
#     this.pileTextH = textAscent()/1.6;
    
    
#     this.pile = function() {
#         textSize(height * 0.08);
#         stroke(0);
        
#         fill(this.pile1textColor);
#         text("Player 1", this.pile1x, this.pileY);
#         line(this.pile1x - this.pileTextW, this.pileY + this.pileTextH, this.pile1x + this.pileTextW, this.pileY + this.pileTextH);
        
        
#         fill(this.pile2textColor);
#         text("Player 2", this.pile2x, this.pileY);
#         line(this.pile2x - this.pileTextW, this.pileY + this.pileTextH, this.pile2x + this.pileTextW, this.pileY + this.pileTextH);
        
#         noStroke();
#         fill(0);
        
#         var pileWidth = 3;
#         var rowCount = 0; // sort pile into rows of {pileWidth}
#         for (var i in this.pile1array) {
#             var w = this.pile1array[i].w;
#             var h = this.pile1array[i].h;
#             var x;
#             if (i % pileWidth === 0) {
#                 rowCount++;
#                 x = this.pile1x - w;
#             }
#             var y = (this.pileY + this.pile1array[i].h) + (rowCount * (h*1.5));
            
#             ellipse(x + ((i % pileWidth) * (w*1.25)), y, w, h);
#         }
        
#         rowCount = 0; // sort pile into rows of {pileWidth}
#         for (var i in this.pile2array) {
#             var w = this.pile2array[i].w;
#             var h = this.pile2array[i].h;
#             var x;
#             if (i % pileWidth === 0) {
#                 rowCount++;
#                 x = this.pile2x - w;
#             }
#             var y = (this.pileY + this.pile2array[i].h) + (rowCount * (h*1.5));
            
#             ellipse(x + ((i % pileWidth) * (w*1.25)), y, w, h);
#         }
        
#     };
    
# };

# var setup = function() {
#     playerBool = false; // false = Player 1 (left), true = Player 2 (right)
#     mouseFlag = true; // true = READY - so the mouseIsPressed only occurs ONCE
#     turnCount = 3; // keeps track of candies taken per turn - MAX 3 / turn
    
#     jar = new Jar(width/2, height/2, 200, 250);
#     num = 13;
#     candySizeW = 30; // define the width of the Candy Object
#     candySizeH = candySizeW / 1.5; // define the height of the Candy Object
    
#     var jarCandyWidth = floor((jar.w / candySizeW) / 2);
#     var rowCount = 0;
#     for (var i = 0; i < num; i++) {
#         // candies.push(new Candy(random(jar.x -jar.w*0.4, jar.x + jar.w*0.4), random(jar.y - jar.h*0.4, jar.y + jar.h*0.4), candySize));
        
#         var x;
#         if (i % jarCandyWidth === 0) {
#             rowCount++;
#             x = jar.y - candySizeW;
#         }
#         var y = (jar.y + (jar.h/2) - candySizeH) - (rowCount * (candySizeH*1.5));
#         candies.push(new Candy(x + ((i % jarCandyWidth) * (candySizeW*1.25)), y, candySizeW));
#     }
    
#     player = new Player();
# };
# setup();

# mousePressed = function() {
#     mouseFlag = false;
# };

# mouseReleased = function() {
#     mouseFlag = true;
# };


# draw = function() {
#     var active = []; // to determine what Objects are active, highest z-index wins
    
#     background(200);
    
#     for (var i = 0; i < candies.length; i++) {
#         candies[i].show();
#         if (candies[i].inRegion()) {
#             active.push(candies[i]);
#         }
#         else {
#             candies[i].highlight = false;
#         }
#     }
    
#     // there's probably a more efficient way to do this....
#     if (active.length > 0) {
#         var current = active[active.length - 1];
#         current.highlight = true;
        
#         if (mouseIsPressed && mouseFlag) {
            
#             if (mouseButton === LEFT && turnCount > 0) {
#                 turnCount--;
#                 // need to stack them into piles
#                 if (!playerBool) {
#                     current.visible = false;
#                     // println(current.w + "\n" + current.h);
                    
#                     player.pile1array.push({w: current.w, h: current.h});
                    
                    
#                     // current.x = 20;
#                     // perhaps make this INVISIBLE, and create a new ellipse in the pile
#                 }
#                 else {
#                     current.visible = false;
                    
#                     player.pile2array.push({w: current.w, h: current.h});
                    
#                     // current.x = width - 20;
#                     // perhaps make this INVISIBLE, and create a new ellipse in the pile
#                 }
#             }
#             // else if (mouseButton === RIGHT) {
#             //     turnCount++;
#             // }
            
#         }
        
#         if (active.length > 1) {
#             for (var i = 0; i < active.length - 1; i++) { // all but the last element
#                 active[i].highlight = false;
#             }
#         }
#     }
    
#     // println("active.length: " + active.length);
    
    
#     jar.show();
#     player.pile();
#     player.turn();
#     player.button();
    
# };


