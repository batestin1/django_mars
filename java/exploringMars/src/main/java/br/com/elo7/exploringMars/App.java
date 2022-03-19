package br.com.elo7.exploringMars;

import java.util.Scanner;

import br.com.elo7.exploringMars.dto.CartesianPlan;
import br.com.elo7.exploringMars.dto.Instruction;
import br.com.elo7.exploringMars.probe.Probe;

public class App 
{
    public static void main( String[] args )
    {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	int axisX = scan.nextInt();
    	int axisY = scan.nextInt();
		
		CartesianPlan cp = Nasa.cartesianPlan(axisX, axisY);
		
			
		int initX = scan.nextInt();
		int initY = scan.nextInt();
		String direction = scan.next();
		Probe p1 = Nasa.probe(initX, initY, direction, cp);
		
		String instructions = scan.next();
		Instruction i1 = Nasa.instruction(instructions);
		
		p1.recieverInstructions(i1);
		
		
		
		

    	
    	
//    	int initX02 = scan.nextInt();
//    	int initY02 = scan.nextInt();
//    	String direction02 = scan.next();
//		Probe p2 = new Probe(initX02, initY02, direction02);
//		
//		String instructions02 = scan.next();
//    	Instruction i2 = new Instruction(instructions02);
//		
//		
//		for (int i = 0; i < i2.getInstruction().split("").length; i++) {
//			String instruction = i2.getInstruction().split("")[i];
//			
//			if ("R".equals(instruction)) {
//				p2.rightMove();
//			} else if ("L".equals(instruction)) {
//				p2.leftMove();
//			} else if ("M".equals(instruction)) {
//				p2.forward(cp.getAxisX(), cp.getAxisY());
//			}
//		}
//		
//		System.out.println("=====");
//		
		System.out.println(p1.getInitX() + " " + p1.getInitY() + " " + p1.getDirection());
//		System.out.println(p2.getInitX() + " " + p2.getInitY() + " " + p2.getDirection());
		


		
    }
}
