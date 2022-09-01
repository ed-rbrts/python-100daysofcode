notes = ['C  ', 'C# ', 'D  ', 'D# ', 'E  ', 'F  ', 'F# ', 'G  ', 'G# ', 'A  ', 'Bb ', 'B  ']		

rot1 = 0.
rot2 = 2/7.
steps = 7
hits = 2

for n in range(14):

    formatted_group = []

    for i in range(hits):

        val = i + rot1;
        val /= hits;
        val *= steps;
        val = round(val);
        val /= 7;
        val *= 12;
        val = round(val);
        val %= 12;

        formatted_group += notes[val] + "    ";

    formatted_group += ("   3 hits:        ")

    for i in range(hits + 1):

        val = i + rot2;
        val /= (hits + 1);
        val *= steps;
        val = round(val);
        val /= 7;
        val *= 12;
        val = round(val);
        val %= 12;

        formatted_group += notes[val] + "    ";





    print(f"{n:03d}:     {''.join(formatted_group) }")
    rot1 += 1/steps
    rot2 += 1/steps



			


	
	    	
	    
	
	