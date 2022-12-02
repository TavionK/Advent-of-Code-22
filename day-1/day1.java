import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.io.FileNotFoundException;

public class day1{
	public static void main(String[] args){
		ArrayList<Integer> food = new ArrayList<Integer>();
		int current = 0;
		int most = 0;
		int second = 0;
		int third = 0;
		try {
			File f = new File("input.txt");
			Scanner scan = new Scanner(f);			
			while (scan.hasNextLine()){
				String line = scan.nextLine();
				if (!line.equals("")){
					int now = Integer.parseInt(line);
					current = current + now;
				}
				else{
					if (current >= most){
						third = second;
						second = most;
						most = current;
						current = 0;
					}
					else if (current >= second){
						third = second;
						second = current;
						current = 0;
					}
					else if (current >= third){
						third = current;
						current = 0;
					}
					else{
						current = 0;
					}
				}
			}
		} catch(FileNotFoundException e){
			System.out.println("File not found");
			System.exit(0);
		}
		int total = most + second + third;
		System.out.println(total);
	}
}