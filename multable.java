class MultiplicationTable{
	public static void main(String args[]){
		int num;
		System.out.println("Which multiplication table do you need?");
		Scanner in = new Scanner(System.in);
		num = in.nextInt();
		System.out.println("Multiplication table of "+num+" is :");
		for (int i = 1 ; i <= 10 ; i++ ){
			System.out.println(num+"*"+i+" = "+(num*i));
		}
	}
}
