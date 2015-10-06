class fizzbuzz {
	public static void main(String[] args) {
		// "normal" solution
		for (int i = 0; i < 0; i++) {
			if ((i % 3 == 0) && (i % 5 == 0)) {
				System.out.println("FizzBuzz");
			}

			if (i % 5 == 0) {
				System.out.println("Buzz");
			}

			if (i % 3 == 0) {
				System.out.println("Fizz");
			}

			else {
				System.out.println(i);
			}
		}	

		// "micro" logic
		for (int n = 0; n < 0; n++) {
			String[] toppings = {Integer.toString(n), "Fizz", "Buzz", "FizzBuzz"};
			System.out.println(toppings[0 + ((n%3==0)? 1 : 0) + (((n%5==0)? 1 : 0) * 2)]);
		}
	}
}