/** Classe para objeto do tipo Probe(sonda) onde ser�o contidos valores e m�todos para o mesmo.
 * Para instanciar esse objeto do tipo Probe � necess�rio informar os seguintes atributos:
 * @param initX - ponto de partida da sonda no eixo X
 * @param initY - ponto de partida da sonda no eixo Y
 * @param direction - dire��o inicial da sonda no plano cartesiano
 */


package br.com.elo7.exploringMars.probe;


import java.util.ArrayList;

import br.com.elo7.exploringMars.dto.CartesianPlan;
import br.com.elo7.exploringMars.dto.Instruction;

public class Probe {
	public int initX;
	public int initY;
	public String direction;
	private ArrayList<String> windRose;
	private CartesianPlan cartesianPlan;
	
	
	public Probe(int initX, int initY, String direction, CartesianPlan cartesianPlan) {
		this.setInitX(initX);
		this.setInitY(initY);
		this.setDirection(direction);
		this.cartesianPlan = cartesianPlan;
		
		this.windRose = new ArrayList<String>();
		windRose.add("N");
		windRose.add("NE");
		windRose.add("E");
		windRose.add("SE");
		windRose.add("S");
		windRose.add("SO");
		windRose.add("W");
		windRose.add("NO");
	}
	
	/** M�todo para mover a sonda em frente 
	 * Esse m�todo verificar� qual a dire��o da sonda e mover� ela a frente  
	 * Ele tamb�m verificar� a partir dos par�metros axisX e axisY se o movimento da sonda est� dentro do plano cartesiano,
	 * n�o ultrapassando os eixos X e Y
	 * se por acaso o movimento for ultrapassar o limite do plano cartesiano, esse movimento ser� ignorado.
	 * @param axisX - valor final/tamanho do eixo X do plano cartesiano
	 * @param axisY - valor final/tamanho do eixo Y do plano cartesiano
	 * 
	 */	
	public void forward(int axisX, int axisY)  {
		if (this.getInitY() <= axisY) {
            if ("N".equals(this.getDirection())) {
                this.setInitY(this.getInitY()+1);
            }
		}
		
		if (this.getInitX() <= axisX) {
            if ("E".equals(this.getDirection())) {
                this.setInitX(this.getInitX()+1);
            }
		}
		
		if (this.getInitY() > 0) {
            if ("S".equals(this.getDirection())) {
                this.setInitY(this.getInitY()-1);
            }
		}
		
		if (this.getInitX() > 0) {
            if ("W".equals(this.getDirection())) {
                this.setInitX(this.getInitX()-1);
            }
		}
		
		if ("NE".equals(this.getDirection())) {
			this.setInitX(this.getInitX()+1);
			this.setInitY(this.getInitY()+1);
		}
		
		if ("SE".equals(this.getDirection())) {
			this.setInitX(this.getInitX()+1);
			this.setInitY(this.getInitY()-1);
		}
		
		if ("SO".equals(this.getDirection())) {
			this.setInitX(this.getInitX()-1);
			this.setInitY(this.getInitY()-1);
		}
		
		if ("NO".equals(this.getDirection())) {
			this.setInitX(this.getInitX()-1);
			this.setInitY(this.getInitY()+1);
		}
		
	}
	
	
	/** M�todo respons�vel por mover a sonda � direita
	 */	
	public void rightMove() {
		int indexDirection = this.windRose.indexOf(direction) + 1;
		if (indexDirection == 8) {
			indexDirection = 0;
		}
		this.setDirection((String) this.windRose.get(indexDirection));
	}
	
	/** M�todo respons�vel por mover a sonda � esquerda
	 */
	public void leftMove() {
		int indexDirection = this.windRose.indexOf(direction) - 1;
		if (indexDirection == -1) {
			indexDirection = 7;
		}
		this.setDirection((String) this.windRose.get(indexDirection));
	}
	
	public void recieverInstructions(Instruction instructions) {
		for (int j = 0; j < instructions.getInstruction().split("").length; j++) {
			String instruction = instructions.getInstruction().split("")[j];
			
			if ("R".equals(instruction)) {
				this.rightMove();
			} else if ("L".equals(instruction)) {
				this.leftMove();
			} else if ("M".equals(instruction)) {
				this.forward(cartesianPlan.getAxisX(), cartesianPlan.getAxisY());
			}
		}
	}
	

	public int getInitX() {
		return initX;
	}




	public void setInitX(int initX) {
		this.initX = initX;
	}




	public int getInitY() {
		return initY;
	}




	public void setInitY(int initY) {
		this.initY = initY;
	}




	public String getDirection() {
		return direction;
	}




	public void setDirection(String direction) {
		this.direction = direction;
	}
	
	
	
	
	public ArrayList<String> getWindRose() {
		return windRose;
	}
	
	
	

	public void setWindRose(ArrayList<String> windRose) {
		this.windRose = windRose;
	}

}
