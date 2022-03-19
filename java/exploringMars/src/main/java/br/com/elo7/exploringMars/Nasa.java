package br.com.elo7.exploringMars;

import br.com.elo7.exploringMars.dto.CartesianPlan;
import br.com.elo7.exploringMars.dto.Instruction;
import br.com.elo7.exploringMars.probe.Probe;

public class Nasa {
	
	public static CartesianPlan cartesianPlan(int axisX, int axisY) {
		return new CartesianPlan(axisX, axisY);
	}
	
	public static Probe probe(int initX, int initY, String direction, CartesianPlan cartesianPlan) {
		return new Probe(initX, initY, direction, cartesianPlan);
	}
	
	public static Instruction instruction(String instruction) {
		return new Instruction(instruction);
	}
	
}
