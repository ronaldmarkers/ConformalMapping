from manim import *

class Figure14(Scene):
    def construct(self):
        plane = ComplexPlane().add_coordinates()

        Number_Plane = NumberPlane(
            background_line_style={
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )

        self.add(plane)

        hor = []
        hora = []
        ver = []
        vera = []

        r=1
        a=3**(0.5) + 2
        vx6 = -7
        vy4 = -4
        x=0
        y=0
        plo = vx6
        pli = vy4

        while vx6 <= 6:
            negx6a = Number_Plane.plot_parametric_curve(
                lambda t: np.array([ ((a*vx6-1)*vx6 + t**2 - a*(a*vx6 - 1))/(t**2+(a*vx6 - 1)**2), (-1)*(t*(vx6-a-a*vx6+1))/(t**2+(a*vx6 - 1)**2), 0]),
                t_range=[-30,30], color=rgb_to_color([0.9999,0.5+(0.5)*((vx6)**2/(plo)**2),0.2])
            )

            hora.append(negx6a)

            negx6 = Number_Plane.plot_parametric_curve(
                lambda t: np.array([ vx6, t, 0]),
                t_range=[-4,4], color=rgb_to_color([0.9999,0.5+(0.5)*((vx6)**2/(plo)**2),0.2])
            )

            hor.append(negx6)
            vx6 += r
            
            self.add(hor[x])
            x += 1

        while vy4 <= 4:
            negy4a = Number_Plane.plot_parametric_curve(
                lambda t: np.array([ ((a*t-1)*t + vy4**2 - a*(a*t - 1))/(vy4**2+(a*t - 1)**2), (-1)*(vy4*(t-a-a*t+1))/(vy4**2+(a*t - 1)**2), 0]),
                t_range=[-30,30], color=rgb_to_color([0.999,0.999,0.1+(0.9)*((vy4)**2/(pli)**2)])
            )

            vera.append(negy4a)

            negy4 = Number_Plane.plot_parametric_curve(
                lambda t: np.array([ t, vy4, 0]),
                t_range=[-7,7], color=rgb_to_color([0.999,0.999,0.1+(0.9)*((vy4)**2/(pli)**2)])
            )

            ver.append(negy4)
            vy4 += r

            self.add(ver[y])
            y += 1

        A = Dot(color=TEAL).move_to(Number_Plane.c2p(1,0))
        self.add(A)
        Ap = Dot(color=TEAL).move_to(Number_Plane.c2p(-1,0))
        Alabel = MathTex("A").next_to(A, UR, 0.1).scale(0.5)
        Aplabel = MathTex("A'").next_to(Ap, UR, 0.1).scale(0.5)
        self.add(Alabel)

        C = Dot(color=TEAL).move_to(Number_Plane.c2p(-1,0))
        self.add(C)
        Cp = Dot(color=TEAL).move_to(Number_Plane.c2p(1,0))
        Clabel = MathTex("C").next_to(C, UR, 0.1).scale(0.5)
        Cplabel = MathTex("C'").next_to(Cp, UR, 0.1).scale(0.5)
        self.add(Clabel)

        B = Dot(color=TEAL).move_to(Number_Plane.c2p(0,1))
        self.add(B)
        Bp = Dot(color=TEAL).move_to(Number_Plane.c2p(0.5,((3)**(1/2))/2))
        Blabel = MathTex("B").next_to(B, UR, 0.1).scale(0.5)
        Bplabel = MathTex("B'").next_to(Bp, UR, 0.1).scale(0.5)
        self.add(Blabel)

        D = Dot(color=TEAL).move_to(Number_Plane.c2p(0,-1))
        self.add(D)
        Dp = Dot(color=TEAL).move_to(Number_Plane.c2p(0.5,(-1)*((3)**(1/2))/2))
        Dlabel = MathTex("D").next_to(D, UR, 0.1).scale(0.5)
        Dplabel = MathTex("D'").next_to(Dp, UR, 0.1).scale(0.5)
        self.add(Dlabel)

        G = Dot(color=TEAL).move_to(Number_Plane.c2p(0.5,0))
        self.add(G)
        Gp = Dot(color=TEAL).move_to(Number_Plane.c2p((-1)*((3)**(1/2))-2,0))
        Glabel = MathTex("G").next_to(G, UR, 0.1).scale(0.5)
        Gplabel = MathTex("G'").next_to(Gp, UR, 0.1).scale(0.5)
        self.add(Glabel)

        E = Dot(color=TEAL).move_to(Number_Plane.c2p(0,0))
        self.add(E)
        Ep = Dot(color=TEAL).move_to(Number_Plane.c2p(((3)**(1/2))+2,0))
        Elabel = MathTex("E").next_to(E, UR, 0.1).scale(0.5)
        Eplabel = MathTex("E'").next_to(Ep, UR, 0.1).scale(0.5)
        self.add(Glabel)

        F = Dot(color=TEAL).move_to(Number_Plane.c2p(0.5,((3)**(1/2))/2))
        self.add(F)
        Fp = Dot(color=TEAL).move_to(Number_Plane.c2p(0,1))
        Flabel = MathTex("F").next_to(F, UR, 0.1).scale(0.5)
        Fplabel = MathTex("F'").next_to(Fp, UR, 0.1).scale(0.5)
        self.add(Glabel)

        ls = 0
        l = []
        while ls < x:
            l.append(ls)
            ls += 1

        ps = 0
        p = []
        while ps < y:
            p.append(ps)
            ps += 1

        self.play(
            *[Transform(hor[x], hora[x]) for x in l],
            *[Transform(ver[x], vera[x]) for x in p],
            Transform(A, Ap),
            Transform(C, Cp),
            Transform(Alabel, Aplabel),
            Transform(Clabel, Cplabel),
            Transform(B, Bp),
            Transform(D, Dp),
            Transform(Blabel, Bplabel),
            Transform(Dlabel, Dplabel),
            Transform(E, Ep),
            Transform(F, Fp),
            Transform(Elabel, Eplabel),
            Transform(Flabel, Fplabel),
            Transform(G, Gp),
            Transform(Glabel, Gplabel)
        )