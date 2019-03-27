package main

import "github.com/astaxie/beego"

type HomeController struct {
	beego.Controller
}

//接受者
func (homeController *HomeController) Get(){
	homeController.Ctx.WriteString("travis build 03/27/2019 16:18\n")
}

func main() {
	beego.Router("/", &HomeController{})
	beego.Run()
}