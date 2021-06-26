import os 
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyrebase

class Modeler_Diffusion:
    def __init__(self):
    #    self.model = 'Diffusion Model'
        self.A = []         
        self.R = []         
        self.F = []          
        self.N = []

    def get_bass_model(self,p, q, M, period):   
        self.A = [0] * period          
        self.R = [0] * period         
        self.F = [0] * period          
        self.N = [0] * period         

        self.A[0] = 0
        self.R[0] = M
        self.F[0] = p
        self.N[0] = M*p
        t = 1

        def get_bass_model_helper(A, R, F, N, t):
            if t == period:
                return N, F, R, A
            else:            
                A[t] = N[t-1] + A[t-1]
                R[t] = M - A[t]
                F[t] = p + q * A[t]/M
                N[t] = F[t] * R[t]

            return get_bass_model_helper(A, R, F, N, t+1)

        self.N, self.F, self.R, self.A = get_bass_model_helper(self.A,
         self.R, self.F, self.N, t)
        return np.array(self.N), np.array(self.A)

    def Upload_NewAdopters_Graphs(self,p,q,period,dataset_name):
        
        t = list(range(0, period))

        fig1 = plt.figure()
        ax1=plt.gca()
        # New Adopters Graph
        ax1.plot(t, self.N, markersize = 4)
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.set_title('Adoption Count over Time Period')
        ax1.set_ylabel("New Adopters")
        ax1.set_xlabel("Years (t)")
        ax1.set_xticks(t)
        fig1.tight_layout()
        fig1.savefig('new adopters graph', dpi = 500)

        fig2 = plt.figure()
        ax2=plt.gca()
        #Cumulative adopters Graph
        ax2.plot(t, self.A, markersize = 4)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.set_title('Adoption Count over Time Period')
        ax2.set_ylabel("Cumulative Adopters")
        ax2.set_xlabel("Years (t)") 
        ax2.set_xticks(t)
        fig2.tight_layout()
        fig2.savefig('cumulative adopters graph', dpi = 500)

        serviceAccountConfig ={
            
                }
        config = {
            
                }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()

        path_local1 = 'D:\\MY DATA\\Desktop\\DB\\Proposal\\new Senior\\Models Deployment\\All Models\\cumulative adopters graph.png'
        path_on_cloud1 = "Graphs/" + str(dataset_name) +" - cumulative graph.png"
        storage.child(path_on_cloud1).put(path_local1)

        path_local2 = 'D:\\MY DATA\\Desktop\\DB\\Proposal\\new Senior\\Models Deployment\\All Models\\new adopters graph.png'
        path_on_cloud2 = "Graphs/" + str(dataset_name) +" - new adopters graph.png"
        storage.child(path_on_cloud2).put(path_local2)