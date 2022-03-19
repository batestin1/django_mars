/** Classe para o objeto Instru��o que definir� as instru��es que a sonda deve receber
 * Classe do tipo DTO - Data Transfor Object
 * 
 * Para instanciar esse objeto do tipo Instruction � necess�rio informar o seguinte atributo:
 * @param instruction - define uma lista de instru��es que deveram ser passadas a sonda
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
