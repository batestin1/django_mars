/** Classe para o objeto Plano Cartesiano que definirá o final/tamanho do plano
 * com seus exios X e Y
 * Classe do tipo DTO - Data Transfor Object
 * 
 * Para instanciar esse objeto do tipo CartesianPlan é necessário informar os seguintes atributos:
 * @param axisX - define o ponto final do plano cartesiano no eixo X
 * @param axisY - define o ponto final do plano cartesiano no eixo Y
 */

package br.com.elo7.exploringMars.dto;

public class CartesianPlan {
	private int axisX;
	private int axisY;
	
	
	public CartesianPlan(int axisX, int axisY) {
		this.setAxisX(axisX);
		this.setAxisY(axisY);
	}
	
	
	
	
	public int getAxisX() {
		return axisX;
	}




	public void setAxisX(int axisX) {
		this.axisX = axisX;
	}




	public int getAxisY() {
		return axisY;
	}




	public void setAxisY(int axisY) {
		this.axisY = axisY;
	}

}
