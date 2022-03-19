/** Classe para o objeto Instrução que definirá as instruções que a sonda deve receber
 * Classe do tipo DTO - Data Transfor Object
 * 
 * Para instanciar esse objeto do tipo Instruction é necessário informar o seguinte atributo:
 * @param instruction - define uma lista de instruções que deveram ser passadas a sonda
 */


package br.com.elo7.exploringMars.dto;



public class Instruction {
	private String instruction;
	
	
	
	public Instruction(String instructions) {
		this.setInstruction(instructions);

	}
	
	

	public String getInstruction() {
		return instruction;
	}



	public void setInstruction(String instructions) {
		this.instruction = instructions;
	}
}
