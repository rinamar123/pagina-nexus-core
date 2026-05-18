
    const lessonTitle = "Introducción a la IA";
    const document = {
        addEventListener: () => {},
        getElementById: () => ({ style: {}, addEventListener: () => {} })
    };
    const window = {};
    
        const lessonTitle = "{{ current_lesson.title|escapejs }}";

        // Dynamic Category Matcher
        function getLessonCategory(title) {
            const t = title.toLowerCase();
            if (t.includes("neurona") || t.includes("perceptrón") || t.includes("perceptron") || t.includes("capa") || t.includes("red") || t.includes("backpropagation") || t.includes("deep") || t.includes("activac") || t.includes("gradient") || t.includes("descen") || t.includes("optimi") || t.includes("cnn") || t.includes("iris") || t.includes("mnist")) {
                return "neural";
            }
            if (t.includes("regres") || t.includes("mínim") || t.includes("minim") || t.includes("error") || t.includes("mse") || t.includes("r2") || t.includes("residual") || t.includes("covar") || t.includes("dummy") || t.includes("dumm") || t.includes("estadíst") || t.includes("estadist") || t.includes("salar") || t.includes("inmobil") || t.includes("precio") || t.includes("multicol") || t.includes("lasso") || t.includes("ridge") || t.includes("regulariz")) {
                return "regression";
            }
            if (t.includes("genét") || t.includes("genet") || t.includes("poblac") || t.includes("cromosom") || t.includes("fitness") || t.includes("cruce") || t.includes("crossover") || t.includes("selecc") || t.includes("mutac") || t.includes("viajer") || t.includes("tsp") || t.includes("elit") || t.includes("mochila") || t.includes("knapsack") || t.includes("ox") || t.includes("reproduc")) {
                return "genetic";
            }
            if (t.includes("lógic") || t.includes("logic") || t.includes("expert") || t.includes("turing") || t.includes("sistem") || t.includes("difus") || t.includes("regla") || t.includes("frenado")) {
                return "logic";
            }
            if (t.includes("enjamb") || t.includes("swarm") || t.includes("pso") || t.includes("partíc") || t.includes("partic") || t.includes("boid") || t.includes("hormig") || t.includes("rastrigin") || t.includes("bio-ia")) {
                return "swarm";
            }
            return "universal";
        }

        // Global functions for Tab switching
        window.switchPlaygroundTab = function(tab) {
            const visualTab = document.getElementById("playground-tab-content-visual");
            const codeTab = document.getElementById("playground-tab-content-code");
            const btnVisual = document.getElementById("tab-btn-visual");
            const btnCode = document.getElementById("tab-btn-code");

            if (tab === 'visual') {
                visualTab.style.display = 'block';
                codeTab.style.display = 'none';
                btnVisual.style.color = 'var(--neon-blue)';
                btnVisual.style.borderBottom = '2px solid var(--neon-blue)';
                btnCode.style.color = 'rgba(255,255,255,0.6)';
                btnCode.style.borderBottom = 'none';
            } else {
                visualTab.style.display = 'none';
                codeTab.style.display = 'flex';
                btnCode.style.color = 'var(--neon-purple)';
                btnCode.style.borderBottom = '2px solid var(--neon-purple)';
                btnVisual.style.color = 'rgba(255,255,255,0.6)';
                btnVisual.style.borderBottom = 'none';
            }
        };

        // Static configuration mapping for each specific category
        const categoryConfigs = {
            "neural": {
                code: "# Simulador de Red Neuronal - Nodo: [TITLE]\nlearning_rate = 0.05\nepochs = 100\nw1 = 0.8\nw2 = 0.4\nbias = -0.5\nactivation = \"sigmoid\"\n\n# Simulación de pérdida y precisión\nfor epoch in range(epochs):\n    loss = round(0.5 / (1 + epoch * learning_rate * 0.1), 4)\n    accuracy = round(0.5 + 0.49 * (1 - 1/(1+epoch*0.05)), 2)\n    if epoch % (epochs // 5) == 0:\n        print(f\"[Epoch {epoch}/{epochs}] Loss: {loss} | Acc: {accuracy}\")",
                html: `
                    <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
                            <!-- Inputs and Sliders -->
                            <div style="display:flex; flex-direction:column; gap:0.8rem; border-right:1px solid rgba(255,255,255,0.05); padding-right:1.2rem;">
                                <h4 style="color:var(--neon-blue); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Hiperparámetros de Entrada</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Learning Rate: <span id="v-lr" style="font-weight:bold; color:var(--neon-blue);">0.05</span></label>
                                    <input type="range" id="s-lr" min="0.01" max="0.5" step="0.01" value="0.05" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Épocas de Entrenamiento: <span id="v-epochs" style="font-weight:bold; color:var(--neon-blue);">100</span></label>
                                    <input type="range" id="s-epochs" min="10" max="500" step="10" value="100" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.8rem;">
                                <h4 style="color:var(--neon-purple); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Pesos y Sesgo</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Peso w1: <span id="v-w1" style="font-weight:bold; color:var(--neon-purple);">0.8</span></label>
                                    <input type="range" id="s-w1" min="-2.0" max="2.0" step="0.1" value="0.8" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                                </div>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Sesgo (Bias): <span id="v-bias" style="font-weight:bold; color:var(--neon-purple);">-0.5</span></label>
                                    <input type="range" id="s-bias" min="-2.0" max="2.0" step="0.1" value="-0.5" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                                </div>
                            </div>
                        </div>

                        <!-- Neural Node graph visualization -->
                        <div style="border-top:1px solid rgba(255,255,255,0.08); padding-top:1.2rem; display:flex; flex-direction:column; align-items:center; background:rgba(0,0,0,0.2); padding:1rem; border-radius:0.8rem; border:1px solid rgba(255,255,255,0.03);">
                            <svg id="neural-layer-svg" width="100%" height="110" viewBox="0 0 400 110" style="background:transparent;">
                                <!-- Connecting Glowing Lines -->
                                <line x1="50" y1="25" x2="200" y2="55" stroke="var(--neon-blue)" stroke-width="2" id="line-w1" opacity="0.6"/>
                                <line x1="50" y1="85" x2="200" y2="55" stroke="var(--neon-blue)" stroke-width="2" id="line-w2" opacity="0.4"/>
                                <line x1="200" y1="55" x2="350" y2="55" stroke="var(--neon-purple)" stroke-width="3" id="line-output" opacity="0.8"/>
                                
                                <!-- Neural Nodes -->
                                <circle cx="50" cy="25" r="16" fill="#09090d" stroke="var(--neon-blue)" stroke-width="2" id="node-x1"/>
                                <text x="50" y="29" fill="white" font-size="8" font-weight="bold" text-anchor="middle">x1</text>

                                <circle cx="50" cy="85" r="16" fill="#09090d" stroke="var(--neon-blue)" stroke-width="2" id="node-x2"/>
                                <text x="50" y="89" fill="white" font-size="8" font-weight="bold" text-anchor="middle">x2</text>

                                <circle cx="200" cy="55" r="22" fill="#09090d" stroke="var(--neon-purple)" stroke-width="3" id="node-neuron"/>
                                <text x="200" y="58" fill="white" font-size="8" font-weight="bold" text-anchor="middle">Σ / σ</text>

                                <circle cx="350" cy="55" r="16" fill="#09090d" stroke="#00ff80" stroke-width="2" id="node-y"/>
                                <text x="350" y="58" fill="white" font-size="8" font-weight="bold" text-anchor="middle">Out</text>
                            </svg>
                            <div style="font-size:0.75rem; color:white; font-weight:bold; margin-top:0.5rem; text-align:center;">
                                Entrada Neta (z): <span id="lbl-z" style="color:var(--neon-blue);">0.30</span> | Activación Sigmoide (a): <span id="lbl-a" style="color:#00ff80;">0.57</span>
                            </div>
                        </div>
                    </div>
                `
            },
            "regression": {
                code: "# Modelado de Regresión y Error - Nodo: [TITLE]\nslope_m = 1.5\nintercept_b = 10.0\nnoise_level = 15.0\ndata_points = 15\n\n# Cálculo de mínimos cuadrados y error cuadrático\nprint(\"Generando puntos de datos experimentales...\")\nx_vals = list(range(1, data_points + 1))\ny_real = [slope_m * x + 10.0 for x in x_vals]\nprint(f\"Ecuación del Modelo Ajustado: Y = {slope_m} * X + {intercept_b}\")",
                html: `
                    <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
                            <!-- Controls -->
                            <div style="display:flex; flex-direction:column; gap:0.8rem; border-right:1px solid rgba(255,255,255,0.05); padding-right:1.2rem;">
                                <h4 style="color:var(--neon-blue); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Pendiente e Intercepto</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Pendiente (m): <span id="v-m" style="font-weight:bold; color:var(--neon-blue);">1.5</span></label>
                                    <input type="range" id="s-m" min="-5.0" max="5.0" step="0.1" value="1.5" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Intercepto (b): <span id="v-b" style="font-weight:bold; color:var(--neon-blue);">10.0</span></label>
                                    <input type="range" id="s-b" min="-50.0" max="50.0" step="1.0" value="10.0" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.8rem;">
                                <h4 style="color:var(--neon-purple); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Datos y Ruido</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Puntos de Datos: <span id="v-pts" style="font-weight:bold; color:var(--neon-purple);">15</span></label>
                                    <input type="range" id="s-pts" min="5" max="30" step="1" value="15" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                                </div>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Nivel de Ruido: <span id="v-noise" style="font-weight:bold; color:var(--neon-purple);">15.0</span></label>
                                    <input type="range" id="s-noise" min="0" max="50" step="1" value="15" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                                </div>
                            </div>
                        </div>

                        <!-- Graphical Scatter and fit line plot -->
                        <div style="border-top:1px solid rgba(255,255,255,0.08); padding-top:1.2rem; display:flex; flex-direction:column; align-items:center; background:rgba(0,0,0,0.25); padding:1rem; border-radius:0.8rem; border:1px solid rgba(255,255,255,0.03);">
                            <svg id="regression-svg" width="100%" height="120" viewBox="0 0 400 120" style="background:#050508; border-radius:0.5rem;">
                                <!-- Fit line and points drawn dynamically -->
                            </svg>
                            <div style="font-size:0.75rem; color:white; font-weight:bold; margin-top:0.5rem; text-align:center;">
                                Error Cuadrático Medio (MSE): <span id="lbl-mse" style="color:var(--neon-purple);">154.2</span> | Coeficiente R²: <span id="lbl-r2" style="color:#00ff80;">0.88</span>
                            </div>
                        </div>
                    </div>
                `
            },
            "genetic": {
                code: "# Algoritmo Genético - Optimización de: [TITLE]\npopulation_size = 50\ngenerations = 30\nmutation_rate = 0.1\ncrossover_point = 4\n\n# Simulación del bucle evolutivo\nprint(\"Iniciando simulación evolutiva...\")\nfor gen in range(generations):\n    fitness = round(0.2 + 0.79 * (1 - 1/(1+gen*0.15)), 3)\n    if gen % 5 == 0:\n        print(f\"Generación {gen}/{generations} | Max Fitness: {fitness}\")",
                html: `
                    <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
                            <!-- Controls -->
                            <div style="display:flex; flex-direction:column; gap:0.8rem; border-right:1px solid rgba(255,255,255,0.05); padding-right:1.2rem;">
                                <h4 style="color:var(--neon-blue); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Parámetros del Algoritmo</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Tamaño de Población: <span id="v-pop" style="font-weight:bold; color:var(--neon-blue);">50</span></label>
                                    <input type="range" id="s-pop" min="10" max="200" step="10" value="50" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Generaciones: <span id="v-gens" style="font-weight:bold; color:var(--neon-blue);">30</span></label>
                                    <input type="range" id="s-gens" min="5" max="100" step="5" value="30" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.8rem;">
                                <h4 style="color:var(--neon-purple); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Operadores Evolutivos</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Tasa de Mutación: <span id="v-mut" style="font-weight:bold; color:var(--neon-purple);">0.10</span></label>
                                    <input type="range" id="s-mut" min="0.01" max="1.0" step="0.01" value="0.10" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                                </div>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Punto de Cruce: <span id="v-crossp" style="font-weight:bold; color:var(--neon-purple);">4</span></label>
                                    <input type="range" id="s-crossp" min="1" max="7" step="1" value="4" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                                </div>
                            </div>
                        </div>

                        <!-- Chromosome visualizer -->
                        <div style="border-top:1px solid rgba(255,255,255,0.08); padding-top:1.2rem; display:flex; flex-direction:column; background:rgba(0,0,0,0.25); padding:1rem; border-radius:0.8rem; border:1px solid rgba(255,255,255,0.03); font-family:monospace; font-size:0.9rem; text-align:center;">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
                                <span style="font-size:0.65rem; color:rgba(255,255,255,0.4); text-transform:uppercase; font-family:sans-serif;">Padre 1 (Cromosoma A):</span>
                                <span id="lbl-chrom1" style="letter-spacing:2px; color:var(--neon-blue); font-weight:bold;">11110000</span>
                            </div>
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
                                <span style="font-size:0.65rem; color:rgba(255,255,255,0.4); text-transform:uppercase; font-family:sans-serif;">Padre 2 (Cromosoma B):</span>
                                <span id="lbl-chrom2" style="letter-spacing:2px; color:var(--neon-purple); font-weight:bold;">00001111</span>
                            </div>
                            <div style="border-top:1px solid rgba(255,255,255,0.08); margin:0.4rem 0;"></div>
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span style="font-size:0.65rem; color:#00ff80; text-transform:uppercase; font-family:sans-serif; font-weight:bold;">Hijo Recombinado + Mutación:</span>
                                <span id="lbl-chrom-hijo" style="letter-spacing:2px; font-weight:bold; color:#00ff80; text-shadow:0 0 8px #00ff80;">11111111</span>
                            </div>
                        </div>
                    </div>
                `
            },
            "logic": {
                code: "# Reglas de Inferencia Lógica y Decisión - Nodo: [TITLE]\ninput_value = 38.5\nthreshold = 37.5\n\n# Evaluación lógica formal\nif input_value >= threshold:\n    print(f\"REGLA ALERTA ACTIVA: {input_value} >= {threshold}\")\n    diagnosis = \"CRÍTICO / ALERTA\"\nelse:\n    diagnosis = \"ESTABLE / SEGURIDAD\"\nprint(f\"Resultado del Motor de Inferencia: {diagnosis}\")",
                html: `
                    <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
                            <!-- Controls -->
                            <div style="display:flex; flex-direction:column; gap:0.8rem; border-right:1px solid rgba(255,255,255,0.05); padding-right:1.2rem;">
                                <h4 style="color:var(--neon-blue); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Parámetros Lógicos</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Valor de Entrada (X): <span id="v-logic-in" style="font-weight:bold; color:var(--neon-blue);">38.5</span></label>
                                    <input type="range" id="s-logic-in" min="10" max="100" step="0.5" value="38.5" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.8rem;">
                                <h4 style="color:var(--neon-purple); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Umbral de Disparo</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Umbral de Corte: <span id="v-logic-th" style="font-weight:bold; color:var(--neon-purple);">37.5</span></label>
                                    <input type="range" id="s-logic-th" min="10" max="100" step="0.5" value="37.5" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                                </div>
                            </div>
                        </div>

                        <!-- Rule activation layout -->
                        <div style="border-top:1px solid rgba(255,255,255,0.08); padding-top:1.2rem; display:flex; align-items:center; justify-content:space-between; background:rgba(0,0,0,0.25); padding:1rem; border-radius:0.8rem; border:1px solid rgba(255,255,255,0.03);">
                            <div>
                                <div style="font-size:0.6rem; color:rgba(255,255,255,0.4); text-transform:uppercase;">Regla Activa:</div>
                                <div style="font-size:0.85rem; color:white; font-weight:bold; font-family:monospace; margin-top:0.2rem;">
                                    IF (X >= Umbral) -> THEN ALERTA
                                </div>
                            </div>
                            <div id="logic-badge" style="padding:0.4rem 0.8rem; border-radius:0.4rem; font-weight:800; font-size:0.7rem; border:1px solid transparent; letter-spacing:0.5px; text-transform:uppercase;">
                                ACTIVADA
                            </div>
                        </div>
                    </div>
                `
            },
            "swarm": {
                code: "# Simulador Enjambre (PSO) - Nodo: [TITLE]\nnum_particles = 20\niterations = 50\nw_inertia = 0.8\nc1_cognitive = 2.0\nc2_social = 2.0\n\n# Simulación de convergencia de partículas hacia el óptimo\nfor it in range(iterations):\n    err = round(10.0 / (1 + it * w_inertia * 0.4), 3)\n    if it % 10 == 0:\n        print(f\"Iteración {it}/{iterations} | Gbest Error: {err}\")",
                html: `
                    <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
                            <!-- Controls -->
                            <div style="display:flex; flex-direction:column; gap:0.8rem; border-right:1px solid rgba(255,255,255,0.05); padding-right:1.2rem;">
                                <h4 style="color:var(--neon-blue); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Factores de Enjambre</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Coeficiente Cognitivo (c1): <span id="v-c1" style="font-weight:bold; color:var(--neon-blue);">2.0</span></label>
                                    <input type="range" id="s-c1" min="0.1" max="4.0" step="0.1" value="2.0" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Coeficiente Social (c2): <span id="v-c2" style="font-weight:bold; color:var(--neon-blue);">2.0</span></label>
                                    <input type="range" id="s-c2" min="0.1" max="4.0" step="0.1" value="2.0" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.8rem;">
                                <h4 style="color:var(--neon-purple); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Coeficiente de Inercia</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Inercia (w): <span id="v-w" style="font-weight:bold; color:var(--neon-purple);">0.8</span></label>
                                    <input type="range" id="s-w" min="0.1" max="1.5" step="0.05" value="0.8" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                                </div>
                            </div>
                        </div>

                        <!-- Graphical Vector / particles plot -->
                        <div style="border-top:1px solid rgba(255,255,255,0.08); padding-top:1.2rem; display:flex; flex-direction:column; align-items:center; background:rgba(0,0,0,0.25); padding:1rem; border-radius:0.8rem; border:1px solid rgba(255,255,255,0.03);">
                            <svg id="swarm-svg" width="100%" height="110" viewBox="0 0 400 110" style="background:#050508; border-radius:0.5rem;">
                                <!-- Vector points drawn dynamically -->
                            </svg>
                            <div style="font-size:0.75rem; color:white; font-weight:bold; margin-top:0.5rem; text-align:center;">
                                Velocidad Media del Enjambre: <span id="lbl-swarm-vel" style="color:var(--neon-blue);">2.34 m/s</span> | Convergencia: <span id="lbl-swarm-conv" style="color:#00ff80;">ALTA</span>
                            </div>
                        </div>
                    </div>
                `
            },
            "universal": {
                code: "# Simulación Universal - Nodo: [TITLE]\nvariable_a = 5.0\nvariable_b = 2.5\nconstant_k = 1.2\n\nresult = round(variable_a * 10.0 + variable_b * 3.1416 * constant_k, 3)\nprint(f\"Resultado del cálculo universal: {result}\")",
                html: `
                    <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
                            <!-- Controls -->
                            <div style="display:flex; flex-direction:column; gap:0.8rem; border-right:1px solid rgba(255,255,255,0.05); padding-right:1.2rem;">
                                <h4 style="color:var(--neon-blue); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Variables Numéricas</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Variable A: <span id="v-ua" style="font-weight:bold; color:var(--neon-blue);">5.0</span></label>
                                    <input type="range" id="s-ua" min="0.0" max="10.0" step="0.1" value="5.0" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                                </div>
                            </div>
                            <div style="display:flex; flex-direction:column; gap:0.8rem;">
                                <h4 style="color:var(--neon-purple); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Constantes del Sistema</h4>
                                <div>
                                    <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Variable B: <span id="v-ub" style="font-weight:bold; color:var(--neon-purple);">2.5</span></label>
                                    <input type="range" id="s-ub" min="0.0" max="10.0" step="0.1" value="2.5" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                                </div>
                            </div>
                        </div>

                        <!-- Mathematical wave SVG representation -->
                        <div style="border-top:1px solid rgba(255,255,255,0.08); padding-top:1.2rem; display:flex; flex-direction:column; align-items:center; background:rgba(0,0,0,0.25); padding:1rem; border-radius:0.8rem; border:1px solid rgba(255,255,255,0.03);">
                            <svg id="universal-svg" width="100%" height="110" viewBox="0 0 400 110" style="background:#050508; border-radius:0.5rem;">
                                <!-- Wave path drawn dynamically -->
                            </svg>
                            <div style="font-size:0.75rem; color:white; font-weight:bold; margin-top:0.5rem; text-align:center;">
                                Valor del Sistema Calculado F(x): <span id="lbl-uval" style="color:#00ff80;">59.42</span>
                            </div>
                        </div>
                    </div>
                `
            }
        };

        // Specific visualizers lookup (original 8 custom ones)
        const visualizers = {
            "Historia de la IA": `
                <div style="display:flex; flex-direction:column; gap:1.5rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.5rem; border-radius:1rem;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size:0.75rem; font-weight:bold; color:var(--neon-blue); letter-spacing:1px;">LÍNEA DE TIEMPO INTERACTIVA</span>
                        <div style="display:flex; align-items:center; gap:0.5rem; width:60%;">
                            <span style="font-size:0.8rem; font-weight:bold; color:var(--neon-blue);" id="timeline-year-label">1950</span>
                            <input type="range" id="timeline-slider" min="0" max="4" step="1" value="0" style="flex:1; accent-color:var(--neon-blue); cursor:pointer;">
                        </div>
                    </div>
                    <div id="timeline-card" style="border:1px solid rgba(255,255,255,0.08); padding:1.2rem; border-radius:0.8rem; background:rgba(0,0,0,0.25); display:flex; gap:1rem; align-items:center; min-height:80px;">
                        <!-- Content will be updated by JS -->
                    </div>
                </div>
            `,
            "Test de Turing": `
                <div style="display:flex; flex-direction:column; gap:1rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                    <div id="chat-messages" style="height:120px; overflow-y:auto; display:flex; flex-direction:column; gap:0.5rem; padding:0.5rem; background:rgba(0,0,0,0.3); border-radius:0.5rem; font-size:0.8rem; border:1px solid rgba(255,255,255,0.03);">
                        <div style="color:var(--neon-blue);">[Sistema]: Iniciando comunicación segura de prueba...</div>
                        <div style="color:#ffaa00;">[Interlocutor]: Hola. Soy un participante del test. ¿Qué te gustaría preguntarme?</div>
                    </div>
                    <div style="display:flex; gap:0.5rem;">
                        <input type="text" id="chat-input" placeholder="Pregúntale algo para ver si es humano..." style="flex:1; background:rgba(255,255,255,0.05); border:1px solid var(--glass-border); padding:0.5rem 1rem; border-radius:0.5rem; color:white; font-size:0.8rem; outline:none; transition:0.3s;" onfocus="this.style.borderColor='var(--neon-blue)'" onblur="this.style.borderColor='var(--glass-border)'">
                        <button id="chat-send-btn" style="background:var(--neon-blue); border:none; color:black; font-weight:bold; padding:0.5rem 1rem; border-radius:0.5rem; cursor:pointer; font-size:0.8rem; transition:0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Enviar</button>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.5rem; border-top:1px solid rgba(255,255,255,0.05); padding-top:0.5rem;">
                        <span style="font-size:0.75rem; color:rgba(255,255,255,0.6);">¿Qué crees que es?</span>
                        <div style="display:flex; gap:0.5rem;">
                            <button onclick="judgeTuring('maquina')" style="background:rgba(255,51,51,0.15); border:1px solid #ff3333; color:#ff3333; font-size:0.7rem; padding:0.3rem 0.6rem; border-radius:0.3rem; cursor:pointer; transition:0.3s; font-weight:bold;" onmouseover="this.style.background='rgba(255,51,51,0.3)'" onmouseout="this.style.background='rgba(255,51,51,0.15)'">Es Máquina 🤖</button>
                            <button onclick="judgeTuring('humano')" style="background:rgba(0,255,128,0.15); border:1px solid #00ff80; color:#00ff80; font-size:0.7rem; padding:0.3rem 0.6rem; border-radius:0.3rem; cursor:pointer; transition:0.3s; font-weight:bold;" onmouseover="this.style.background='rgba(0,255,128,0.3)'" onmouseout="this.style.background='rgba(0,255,128,0.15)'">Es Humano 👤</button>
                        </div>
                    </div>
                    <div id="turing-verdict" style="display:none; font-size:0.8rem; text-align:center; font-weight:bold; padding:0.8rem; border-radius:0.5rem; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05);"></div>
                </div>
            `,
            "Tu Primera Neurona": `
                <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
                        <!-- Inputs y Pesos -->
                        <div style="display:flex; flex-direction:column; gap:0.8rem; border-right:1px solid rgba(255,255,255,0.05); padding-right:1rem;">
                            <h4 style="color:var(--neon-blue); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Entradas (Inputs)</h4>
                            <div>
                                <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">x1 (Horas de Estudio): <span id="val-x1" style="font-weight:bold; color:white;">1.0</span></label>
                                <input type="range" id="slide-x1" min="0" max="1" step="0.1" value="1.0" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                            </div>
                            <div>
                                <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">x2 (Asistencia Clases): <span id="val-x2" style="font-weight:bold; color:white;">0.5</span></label>
                                <input type="range" id="slide-x2" min="0" max="1" step="0.1" value="0.5" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                            </div>
                        </div>
                        
                        <div style="display:flex; flex-direction:column; gap:0.8rem;">
                            <h4 style="color:var(--neon-purple); margin:0; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Parámetros Aprendidos</h4>
                            <div>
                                <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Peso w1: <span id="val-w1" style="font-weight:bold; color:white;">0.8</span></label>
                                <input type="range" id="slide-w1" min="-2" max="2" step="0.1" value="0.8" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                            </div>
                            <div>
                                <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Peso w2: <span id="val-w2" style="font-weight:bold; color:white;">0.4</span></label>
                                <input type="range" id="slide-w2" min="-2" max="2" step="0.1" value="0.4" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                            </div>
                            <div>
                                <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Sesgo (Bias): <span id="val-bias" style="font-weight:bold; color:white;">-0.5</span></label>
                                <input type="range" id="slide-bias" min="-2" max="2" step="0.1" value="-0.5" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                            </div>
                        </div>
                    </div>
                    
                    <!-- Live Neural Output Visualization -->
                    <div style="border-top:1px solid rgba(255,255,255,0.08); padding-top:1rem; display:flex; align-items:center; justify-content:space-between; background:rgba(0,0,0,0.25); padding:1rem; border-radius:0.8rem; border:1px solid rgba(255,255,255,0.03);">
                        <div>
                            <div style="font-size:0.6rem; color:rgba(255,255,255,0.4); text-transform:uppercase; font-family:monospace; letter-spacing:0.5px;">Fórmula: z = x1·w1 + x2·w2 + bias | a = σ(z)</div>
                            <div style="font-size:0.8rem; color:white; font-weight:bold; margin-top:0.3rem;">
                                Entrada Neta (z): <span id="calc-z" style="color:var(--neon-blue);">0.30</span>
                            </div>
                            <div style="font-size:0.8rem; color:white; font-weight:bold; margin-top:0.2rem;">
                                Activación Sigmoidal (a): <span id="calc-a" style="color:var(--neon-purple);">0.57</span>
                            </div>
                        </div>
                        <div id="neuron-fire-badge" style="padding:0.4rem 0.8rem; border-radius:0.4rem; font-weight:800; font-size:0.7rem; border:1px solid transparent; letter-spacing:0.5px; text-transform:uppercase;">
                            ACTIVADA
                        </div>
                    </div>
                </div>
            `,
            "Estadística Predictiva": `
                <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                    <div style="display:flex; flex-direction:column; gap:0.4rem;">
                        <label style="font-size:0.75rem; color:rgba(255,255,255,0.8); font-weight:bold;">Ingresa valores numéricos separados por comas:</label>
                        <div style="display:flex; gap:0.5rem;">
                            <input type="text" id="stats-input-data" value="10, 15, 20, 25, 30" style="flex:1; background:#111; border:1px solid var(--glass-border); padding:0.4rem 0.8rem; border-radius:0.5rem; color:white; font-size:0.8rem; font-family:monospace; outline:none; letter-spacing:0.5px;">
                            <button id="stats-calc-btn" style="background:var(--neon-blue); border:none; color:black; font-weight:bold; padding:0.4rem 1rem; border-radius:0.5rem; cursor:pointer; font-size:0.8rem; transition:0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Calcular</button>
                        </div>
                    </div>
                    
                    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.8rem; text-align:center;">
                        <div style="background:rgba(0,0,0,0.25); padding:0.6rem; border-radius:0.5rem; border:1px solid rgba(255,255,255,0.03);">
                            <div style="font-size:0.6rem; color:rgba(255,255,255,0.5); text-transform:uppercase;">Media (μ)</div>
                            <div id="stats-mean" style="font-size:1.1rem; font-weight:bold; color:var(--neon-blue); margin-top:0.2rem;">20.0</div>
                        </div>
                        <div style="background:rgba(0,0,0,0.25); padding:0.6rem; border-radius:0.5rem; border:1px solid rgba(255,255,255,0.03);">
                            <div style="font-size:0.6rem; color:rgba(255,255,255,0.5); text-transform:uppercase;">Varianza (σ²)</div>
                            <div id="stats-variance" style="font-size:1.1rem; font-weight:bold; color:var(--neon-purple); margin-top:0.2rem;">100.0</div>
                        </div>
                        <div style="background:rgba(0,0,0,0.25); padding:0.6rem; border-radius:0.5rem; border:1px solid rgba(255,255,255,0.03);">
                            <div style="font-size:0.6rem; color:rgba(255,255,255,0.5); text-transform:uppercase;">Desv. Estándar (σ)</div>
                            <div id="stats-stddev" style="font-size:1.1rem; font-weight:bold; color:#00ff80; margin-top:0.2rem;">10.0</div>
                        </div>
                    </div>

                    <!-- Dynamic Mini Chart -->
                    <div id="stats-chart-canvas" style="height:110px; background:rgba(0,0,0,0.4); border-radius:0.5rem; position:relative; overflow:hidden; border:1px solid rgba(255,255,255,0.03);">
                        <!-- Bars and mean line will be placed here dynamically -->
                    </div>
                </div>
            `,
            "Variables Dummy": `
                <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                    <p style="font-size:0.75rem; color:rgba(255,255,255,0.6); margin:0;">Establece la ciudad categórica de los tres estudiantes para generar el mapeo matricial binario (One-Hot Encoding) en tiempo real:</p>
                    <div style="display:flex; flex-direction:column; gap:0.6rem;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:0.75rem; font-weight:bold; color:white;">Estudiante 1 (Residencia):</span>
                            <select id="dummy-e1" style="background:#111; color:white; border:1px solid var(--glass-border); padding:0.25rem 0.5rem; border-radius:0.4rem; font-size:0.75rem; outline:none;">
                                <option value="Medellín">Medellín</option>
                                <option value="Cali">Cali</option>
                                <option value="Bogotá">Bogotá</option>
                            </select>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:0.75rem; font-weight:bold; color:white;">Estudiante 2 (Residencia):</span>
                            <select id="dummy-e2" style="background:#111; color:white; border:1px solid var(--glass-border); padding:0.25rem 0.5rem; border-radius:0.4rem; font-size:0.75rem; outline:none;">
                                <option value="Cali" selected>Cali</option>
                                <option value="Medellín">Medellín</option>
                                <option value="Bogotá">Bogotá</option>
                            </select>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:0.75rem; font-weight:bold; color:white;">Estudiante 3 (Residencia):</span>
                            <select id="dummy-e3" style="background:#111; color:white; border:1px solid var(--glass-border); padding:0.25rem 0.5rem; border-radius:0.4rem; font-size:0.75rem; outline:none;">
                                <option value="Bogotá">Bogotá</option>
                                <option value="Medellín">Medellín</option>
                                <option value="Cali">Cali</option>
                            </select>
                        </div>
                    </div>

                    <!-- Render One-Hot Matrix -->
                    <table style="width:100%; border-collapse:collapse; font-size:0.75rem; text-align:center; background:rgba(0,0,0,0.25); border-radius:0.5rem; overflow:hidden; border:1px solid rgba(255,255,255,0.03);">
                        <thead>
                            <tr style="background:rgba(255,255,255,0.05); color:rgba(255,255,255,0.6); font-size:0.65rem; border-bottom:1px solid rgba(255,255,255,0.05);">
                                <th style="padding:0.5rem 0.8rem; text-align:left;">Estudiante</th>
                                <th style="padding:0.5rem;">Dummy_Bogotá</th>
                                <th style="padding:0.5rem;">Dummy_Cali</th>
                                <th style="padding:0.5rem;">Dummy_Medellín</th>
                            </tr>
                        </thead>
                        <tbody id="dummy-matrix-body">
                            <!-- Rows will be injected by JS -->
                        </tbody>
                    </table>
                </div>
            `,
            "Regresión Logística": `
                <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
                        <div>
                            <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Entrada Neta (z): <span id="val-log-z" style="color:var(--neon-blue); font-weight:bold;">0.0</span></label>
                            <input type="range" id="slide-log-z" min="-6" max="6" step="0.2" value="0.0" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                        </div>
                        <div>
                            <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Umbral de Corte: <span id="val-log-threshold" style="color:var(--neon-purple); font-weight:bold;">0.50</span></label>
                            <input type="range" id="slide-log-threshold" min="0.1" max="0.9" step="0.05" value="0.5" style="width:100%; accent-color:var(--neon-purple); cursor:pointer;">
                        </div>
                    </div>

                    <!-- Dynamic Sigmoid Plot SVG -->
                    <div style="position:relative; text-align:center;">
                        <svg id="sigmoid-svg" width="100%" height="130" viewBox="0 0 300 130" style="background:#050508; border-radius:0.6rem; border:1px solid rgba(255,255,255,0.03);">
                            <!-- Sigmoid curve drawn dynamically -->
                        </svg>
                    </div>

                    <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(0,0,0,0.25); padding:0.8rem; border-radius:0.5rem; border:1px solid rgba(255,255,255,0.03);">
                        <div>
                            <div style="font-size:0.6rem; color:rgba(255,255,255,0.4); text-transform:uppercase; font-family:monospace;">Probabilidad Resultante:</div>
                            <div id="log-prob" style="font-size:1rem; font-weight:bold; color:var(--neon-blue); margin-top:0.1rem;">50.0%</div>
                        </div>
                        <div id="log-class-badge" style="padding:0.4rem 0.8rem; border-radius:0.4rem; font-weight:800; font-size:0.7rem; text-transform:uppercase; border:1px solid transparent; letter-spacing:0.5px;">
                            CLASE
                        </div>
                    </div>
                </div>
            `,
            "Cruce (Crossover)": `
                <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.8rem;">
                        <div>
                            <label style="font-size:0.7rem; color:rgba(255,255,255,0.5); display:block; margin-bottom:0.2rem;">Cromosoma Padre 1:</label>
                            <input type="text" id="cross-p1" value="11111111" style="width:100%; background:#111; border:1px solid var(--glass-border); padding:0.3rem; border-radius:0.4rem; color:var(--neon-blue); font-family:monospace; font-weight:bold; outline:none; font-size:0.85rem; text-align:center; letter-spacing:1px;">
                        </div>
                        <div>
                            <label style="font-size:0.7rem; color:rgba(255,255,255,0.5); display:block; margin-bottom:0.2rem;">Cromosoma Padre 2:</label>
                            <input type="text" id="cross-p2" value="00000000" style="width:100%; background:#111; border:1px solid var(--glass-border); padding:0.3rem; border-radius:0.4rem; color:var(--neon-purple); font-family:monospace; font-weight:bold; outline:none; font-size:0.85rem; text-align:center; letter-spacing:1px;">
                        </div>
                    </div>
                    <div>
                        <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Punto de Corte (Crossover): <span id="val-cross-point" style="color:#00ff80; font-weight:bold;">4</span></label>
                        <input type="range" id="slide-cross-point" min="1" max="7" step="1" value="4" style="width:100%; accent-color:#00ff80; cursor:pointer;">
                    </div>

                    <!-- Dynamic Visualization of recombination -->
                    <div style="display:flex; flex-direction:column; gap:0.8rem; background:rgba(0,0,0,0.25); padding:1rem; border-radius:0.8rem; border:1px solid rgba(255,255,255,0.03); font-family:monospace; font-size:1.05rem; text-align:center;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:0.65rem; color:rgba(255,255,255,0.4); font-family:sans-serif; text-transform:uppercase;">Padre 1:</span>
                            <span id="cross-vis-p1" style="letter-spacing:3px;"></span>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:0.65rem; color:rgba(255,255,255,0.4); font-family:sans-serif; text-transform:uppercase;">Padre 2:</span>
                            <span id="cross-vis-p2" style="letter-spacing:3px;"></span>
                        </div>
                        <div style="border-top:1px solid rgba(255,255,255,0.08); margin:0.3rem 0;"></div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:0.65rem; color:#00ff80; font-family:sans-serif; font-weight:bold; text-transform:uppercase;">Hijo Recombinado:</span>
                            <span id="cross-vis-hijo" style="letter-spacing:3px; font-weight:bold; color:#00ff80;"></span>
                        </div>
                    </div>
                </div>
            `,
            "Mutación": `
                <div style="display:flex; flex-direction:column; gap:1.2rem; background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.05); padding:1.2rem; border-radius:1rem;">
                    <div>
                        <label style="font-size:0.7rem; color:rgba(255,255,255,0.5); display:block; margin-bottom:0.2rem;">Cromosoma del Individuo (Binario):</label>
                        <div style="display:flex; gap:0.5rem;">
                            <input type="text" id="mut-indiv" value="10101010" style="flex:1; background:#111; border:1px solid var(--glass-border); padding:0.3rem; border-radius:0.4rem; color:white; font-family:monospace; font-weight:bold; outline:none; font-size:0.85rem; text-align:center; letter-spacing:2px;">
                            <button id="mut-random-btn" style="background:var(--neon-purple); border:none; color:white; font-weight:bold; padding:0.3rem 0.8rem; border-radius:0.4rem; cursor:pointer; font-size:0.7rem; transition:0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Mutación Rnd</button>
                        </div>
                    </div>
                    <div>
                        <label style="font-size:0.7rem; color:rgba(255,255,255,0.6); display:flex; justify-content:space-between; margin-bottom:0.2rem;">Mutar Bit en el Índice: <span id="val-mut-index" style="color:var(--neon-blue); font-weight:bold;">3</span></label>
                        <input type="range" id="slide-mut-index" min="0" max="7" step="1" value="3" style="width:100%; accent-color:var(--neon-blue); cursor:pointer;">
                    </div>

                    <!-- Dynamic Visualization of Mutation -->
                    <div style="display:flex; flex-direction:column; gap:0.8rem; background:rgba(0,0,0,0.25); padding:1rem; border-radius:0.8rem; border:1px solid rgba(255,255,255,0.03); font-family:monospace; font-size:1.05rem; text-align:center;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:0.65rem; color:rgba(255,255,255,0.4); font-family:sans-serif; text-transform:uppercase;">Original:</span>
                            <span id="mut-vis-orig" style="letter-spacing:3px;"></span>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:0.65rem; color:rgba(255,255,255,0.4); font-family:sans-serif; font-weight:bold; text-transform:uppercase;">Mutado:</span>
                            <span id="mut-vis-mut" style="letter-spacing:3px; font-weight:bold; color:var(--neon-purple);"></span>
                        </div>
                    </div>
                </div>
            `
        };

        // Predefined Challenges Lookup
        const challenges = {
            "Historia de la IA": {
                prompt: "Analiza la diferencia fundamental entre el enfoque de la Inteligencia Artificial Simbólica y el Conexionista. A partir del siguiente esquema conceptual:",
                code: `# Enfoque A: Representación basada en lógica formal, reglas semánticas y sistemas expertos deductivos.\n# Enfoque B: Optimización probabilística de capas neuronales que aprenden de la experiencia empírica.`,
                choices: [
                    "El Enfoque A es Simbólico y el Enfoque B es Conexionista.",
                    "El Enfoque A es Conexionista y el Enfoque B es Simbólico.",
                    "Ambos enfoques representan redes de inferencia cuántica no determinista."
                ],
                correct: 0,
                feedback: "¡EXCELENTE! El enfoque simbólico (IA clásica) opera traduciendo el conocimiento humano en reglas lógicas condicionales. El conexionista (redes neuronales) prescinde de reglas rígidas y calcula la probabilidad mediante pesos optimizados estadísticamente."
            },
            "Test de Turing": {
                prompt: "Examina el flujo de diálogo en Python diseñado para evaluar a un agente candidato en el Test de Turing:",
                code: `def evaluar_dialogo(respuestas_agente):\n    score = 0\n    for r in respuestas_agente:\n        if es_indistinguible_de_humano(r):\n            score += 1\n    return score >= len(respuestas_agente) * 0.7`,
                choices: [
                    "Si el agente obtiene un score superior al 70%, se le considera indistinguible de un humano y supera la prueba.",
                    "El script da error porque no evalúa la velocidad de cálculo binario de la CPU.",
                    "La función siempre retorna False independientemente del desempeño del chatbot."
                ],
                correct: 0,
                feedback: "¡CORRECTO! En el Test de Turing, el criterio de éxito se define por la incapacidad del evaluador humano para distinguir estadísticamente entre la máquina y el humano. Un acierto por encima del 70% en diálogos es el estándar de éxito formal."
            },
            "Tu Primera Neurona": {
                prompt: "Utilizando la fórmula básica de entrada neta (z = sum(x_i * w_i) + bias) para una neurona con dos entradas, calcula el valor de z con los datos indicados en la visualización:",
                code: `x1 = 1.0,  w1 = 0.5\nx2 = 0.0,  w2 = -0.2\nbias = 0.1\n\nz = (x1 * w1) + (x2 * w2) + bias`,
                choices: [
                    "z = 0.6",
                    "z = 0.4",
                    "z = 0.3"
                ],
                correct: 0,
                feedback: "¡EXCELENTE CÁLCULO! Multiplicamos 1.0 * 0.5 = 0.5. Luego 0.0 * -0.2 = 0.0. Sumamos ambos resultados (0.5 + 0.0) and añadimos el sesgo (+0.1) dando un total de 0.6. Este valor resultante (z) es el que ingresa a la función de activación Sigmoide."
            },
            "Estadística Predictiva": {
                prompt: "Considera la siguiente colección de datos empíricos cargados para un modelado predictivo simple en Python:",
                code: `datos = [2, 4, 4, 4, 5, 5, 7, 9]\n\n# Ecuación matemática: Media = Sumatoria(datos) / N`,
                choices: [
                    "La media de la muestra es 5.0",
                    "La media de la muestra es 4.5",
                    "La media de la muestra es 6.0"
                ],
                correct: 0,
                feedback: "¡CORRECTO! Sumamos todos los valores de la lista: 2 + 4 + 4 + 4 + 5 + 5 + 7 + 9 = 40. Dividimos por la cantidad total de elementos (8) obteniendo una media de 5.0."
            },
            "Variables Dummy": {
                prompt: "Dado un conjunto de datos que registra la ciudad de residencia de tres estudiantes, analiza el código de One-Hot Encoding:",
                code: `ciudades = ['Medellín', 'Medellín', 'Cali']\n# Al codificar con pd.get_dummies, ¿cómo queda representado 'Cali' en el vector binario?`,
                choices: [
                    "[Cali = 1, Medellín = 0]",
                    "[Cali = 0, Medellín = 1]",
                    "[Cali = 1, Medellín = 1]"
                ],
                correct: 0,
                feedback: "¡FANTÁSTICO! Las variables dummy crean una columna para cada categoría única. Cali se convierte en la columna activa (1) y Medellín permanece inactiva (0), evitando conflictos dimensionales en el regresor lineal."
            },
            "Regresión Logística": {
                prompt: "Estudia el fragmento de código que computa la probabilidad de aprobación en base al umbral estándar de decisión logística:",
                code: `probabilidad = 0.73\numbral_decision = 0.50\n\naprobado = probabilidad >= umbral_decision`,
                choices: [
                    "aprobado = True (Clase 1 / Evento exitoso)",
                    "aprobado = False (Clase 0 / Evento fallido)",
                    "El resultado es nulo porque falta calcular la exponencial de Euler."
                ],
                correct: 0,
                feedback: "¡IMPECABLE! Como la probabilidad calculada por la función sigmoide (0.73) supera el umbral estándar (0.50), el perceptrón clasifica el evento de forma binaria dentro de la clase activa (Clase 1, True)."
            },
            "Cruce (Crossover)": {
                prompt: "Analiza la siguiente recombinación génica realizada en el punto de corte (índice 2) en un algoritmo genético:",
                code: `padre1 = [1, 1, 1, 1]\npadre2 = [0, 0, 0, 0]\npunto_cruce = 2\n\nhijo = padre1[:punto_cruce] + padre2[punto_cruce:]`,
                choices: [
                    "hijo = [1, 1, 0, 0]",
                    "hijo = [1, 0, 1, 0]",
                    "hijo = [0, 0, 1, 1]"
                ],
                correct: 0,
                feedback: "¡EXCELENTE! El cruce de un solo punto toma la primera mitad de los genes de Padre 1 (índices 0 y 1: [1, 1]) y la segunda mitad de los genes de Padre 2 (índices 2 y 3: [0, 0]), ensamblando perfectamente al hijo [1, 1, 0, 0]."
            },
            "Mutación": {
                prompt: "Estudia el siguiente código que simula la mutación de un individuo binario mediante inversión de bit en el índice especificado:",
                code: `individuo = [1, 0, 1, 0]\nindice_mutar = 1\n\n# Invertir bit en indice_mutar\nindividuo[indice_mutar] = 1 if individuo[indice_mutar] == 0 else 0`,
                choices: [
                    "individuo mutado = [1, 1, 1, 0]",
                    "individuo mutado = [1, 0, 1, 0]",
                    "individuo mutado = [0, 0, 1, 0]"
                ],
                correct: 0,
                feedback: "¡BRILLANTE! El gen original en el índice 1 era 0. Tras aplicar el operador genético de mutación por inversion de bit, se convierte en 1, dando como resultado el vector binario [1, 1, 1, 0]."
            }
        };

        // Fallback Category Challenges
        const defaultChallenges = {
            "neural": {
                prompt: "Analiza el comportamiento de una red neuronal artificial. Si incrementamos positivamente el sesgo (bias) en el código sandbox de arriba, ¿cuál es el efecto en la activación neuronal?",
                choices: [
                    "La neurona requiere menor excitación de entrada neta para activarse y dispararse.",
                    "La neurona se inhibe y nunca alcanzará el disparo.",
                    "Los pesos w1 y w2 se anulan automáticamente reduciéndose a cero."
                ],
                correct: 0,
                feedback: "¡EXCELENTE! El sesgo (bias) funciona como un umbral de corte. Aumentar el bias positivamente facilita la activación (disparo) de la neurona sigmoidal o ReLU bajo menores valores de entradas."
            },
            "regression": {
                prompt: "Estudia la influencia del parámetro de la pendiente (slope_m) en tu regresión lineal. Si modificamos este parámetro por un número menor a cero en la consola, ¿cuál es la correlación resultante?",
                choices: [
                    "Correlación inversa o negativa: al incrementarse X, el valor de Y disminuye.",
                    "Correlación directa o positiva: al incrementarse X, el valor de Y aumenta.",
                    "El Error Cuadrático Medio (MSE) se reduce a cero de forma matemática."
                ],
                correct: 0,
                feedback: "¡CORRECTO! Una pendiente negativa (m < 0) define una relación inversa entre ambas variables continuas; la recta de regresión desciende de izquierda a derecha."
            },
            "genetic": {
                prompt: "Analiza el comportamiento del operador de mutación en algoritmos evolutivos. Si ajustamos la tasa de mutación a su valor máximo de 1.0 (100%), ¿qué ocurre con el proceso de búsqueda?",
                choices: [
                    "La búsqueda evolutiva se degrada en una búsqueda puramente aleatoria sin convergencia estable.",
                    "El algoritmo encontrará la solución perfecta en la primera iteración.",
                    "Los descendientes serán copias binarias idénticas sin variación genética."
                ],
                correct: 0,
                feedback: "¡IMPECABLE! Una tasa de mutación excesivamente alta destruye el principio de herencia. Los mejores genes descubiertos se corrompen constantemente, degradando el algoritmo en un muestreo aleatorio descontrolado."
            },
            "logic": {
                prompt: "En los sistemas inteligentes difusos (Fuzzy Logic), ¿cómo se define la lógica en comparación con la lógica formal booleana?",
                choices: [
                    "Permite grados de pertenencia y verdad parciales expresados como valores continuos entre 0 y 1.",
                    "Es estrictamente binaria, forzando cada estado a ser únicamente 0 (Falso) o 1 (Verdadero).",
                    "No permite el procesamiento de números decimales debido a limitaciones físicas de la CPU."
                ],
                correct: 0,
                feedback: "¡CORRECTO! La lógica difusa representa la incertidumbre y gradaciones semánticas del razonamiento humano mediante funciones de pertenencia continuas en el intervalo real [0, 1]."
            },
            "swarm": {
                prompt: "En la optimización por enjambre de partículas (PSO), ¿qué rol cumple el parámetro de inercia (w) en la convergencia de las partículas?",
                choices: [
                    "Modera el impacto de la velocidad anterior, balanceando la exploración global y explotación local.",
                    "Fuerza a todas las partículas a teletransportarse al punto central del mapa.",
                    "Elimina al enjambre de partículas que tengan un fitness menor al promedio."
                ],
                correct: 0,
                feedback: "¡EXCELENTE! La inercia w controla el momento de la partícula. Valores altos promueven la exploración de nuevas áreas del espacio de búsqueda, mientras valores bajos favorecen el refinamiento local."
            },
            "universal": {
                prompt: "En ciencias de la computación e Inteligencia Artificial, ¿por qué es importante normalizar la escala de las variables continuas antes de realizar una optimización?",
                choices: [
                    "Para homogeneizar las escalas, permitiendo que el optimizador converja de forma rápida y matemáticamente estable.",
                    "Para remover los registros duplicados y nulos de nuestra base de datos de manera automática.",
                    "Para forzar que el modelo sea puramente lineal sin importar las correlaciones."
                ],
                correct: 0,
                feedback: "¡EXCELENTE PROTOCOLO! Escalar variables (por ejemplo, a rangos [0,1] o puntuación Z) previene que variables de magnitudes masivas dominen de forma artificial la función de costo y desestabilicen los gradientes."
            }
        };

        // Main Controller Loader
        document.addEventListener("DOMContentLoaded", () => {
            const visualizerBox = document.getElementById("visualizerBox");
            const visualizerCanvas = document.getElementById("visualizerCanvas");
            const challengeBox = document.getElementById("challengeBox");
            const challengePrompt = document.getElementById("challengePrompt");
            const challengeCodeBox = document.getElementById("challengeCodeBox");
            const challengeChoices = document.getElementById("challengeChoices");

            // 1. Sanitize lesson title and match category
            let cleanTitle = lessonTitle.replace(/^\[[A-Z]+\]\s*/, "");
            if (cleanTitle.includes("Introducción a la IA") || cleanTitle.includes("Historia de la IA")) {
                cleanTitle = "Historia de la IA";
            } else if (cleanTitle.includes("Test de Turing")) {
                cleanTitle = "Test de Turing";
            }

            const category = getLessonCategory(cleanTitle);
            const isCustomVisualizer = visualizers[cleanTitle] !== undefined;

            // 2. Build multi-tab container structure in visualizerCanvas
            const visualTabContent = isCustomVisualizer ? visualizers[cleanTitle] : (categoryConfigs[category] ? categoryConfigs[category].html : categoryConfigs["universal"].html);
            const defaultCode = isCustomVisualizer ? `\n# Simulador Interactivo - Nodo de Clase: \${cleanTitle}\n# Modifica los parámetros en la pestaña visual para ver el código o edita aquí y simula!\n` : (categoryConfigs[category] ? categoryConfigs[category].code.replace("[TITLE]", cleanTitle) : categoryConfigs["universal"].code.replace("[TITLE]", cleanTitle));

            visualizerCanvas.innerHTML = `
                <div class="interactive-playground-container" style="display:flex; flex-direction:column; gap:1.2rem;">
                    <!-- Tab Navigation -->
                    <div class="playground-tabs" style="display:flex; gap:0.5rem; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:0.5rem;">
                        <button id="tab-btn-visual" class="playground-tab-btn" onclick="switchPlaygroundTab('visual')" style="background:none; border:none; color:var(--neon-blue); border-bottom:2px solid var(--neon-blue); padding:0.5rem 1rem; font-weight:bold; cursor:pointer; font-size:0.8rem; font-family:'Space Grotesk', sans-serif; transition:0.3s; outline:none;">📊 Visualizador Playground</button>
                        <button id="tab-btn-code" class="playground-tab-btn" onclick="switchPlaygroundTab('code')" style="background:none; border:none; color:rgba(255,255,255,0.6); padding:0.5rem 1rem; cursor:pointer; font-size:0.8rem; font-family:'Space Grotesk', sans-serif; transition:0.3s; outline:none;">💻 Simular Código en Vivo</button>
                    </div>
                    
                    <!-- Visual Tab content area -->
                    <div id="playground-tab-content-visual" style="display:block;">
                        \${visualTabContent}
                    </div>
                    
                    <!-- Code Editor Tab content area -->
                    <div id="playground-tab-content-code" style="display:none; flex-direction:column; gap:1rem;">
                        <div style="font-size:0.75rem; color:rgba(255,255,255,0.5);">Modifica las variables numéricas en el código Python de abajo y haz clic en "Ejecutar Simulación" para recalcular el modelo en tiempo real:</div>
                        <textarea id="code-sandbox-editor" style="width:100%; height:130px; background:#070709; border:1px solid rgba(255,255,255,0.1); border-radius:0.6rem; color:#a9ffb2; font-family:'Courier New', monospace; font-size:0.8rem; padding:0.8rem; resize:vertical; outline:none;" spellcheck="false">\${defaultCode}</textarea>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <button id="code-sandbox-run-btn" onclick="runCodeSandbox()" style="background:var(--neon-blue); border:none; color:black; font-weight:bold; padding:0.5rem 1.2rem; border-radius:0.4rem; cursor:pointer; font-size:0.8rem; transition:0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">▶️ Ejecutar Simulación</button>
                            <span style="font-size:0.7rem; color:var(--neon-purple); font-family:monospace;">sandbox://python_engine</span>
                        </div>
                        <div style="background:#030305; border:1px solid rgba(255,255,255,0.05); border-radius:0.6rem; padding:0.8rem;">
                            <div style="font-size:0.65rem; color:rgba(255,255,255,0.4); text-transform:uppercase; letter-spacing:0.5px; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:0.3rem; margin-bottom:0.5rem; display:flex; justify-content:space-between;">
                                <span>Salida de Consola</span>
                                <span id="sandbox-running-indicator" style="color:var(--neon-blue); display:none; animation: pulse 1s infinite;">● PROCESANDO...</span>
                            </div>
                            <pre id="code-sandbox-terminal" style="margin:0; font-family:'Courier New', monospace; font-size:0.75rem; color:#e0e0e0; min-height:60px; white-space:pre-wrap; max-height:120px; overflow-y:auto;"></pre>
                        </div>
                    </div>
                </div>
            `;

            // Always display the visualizer box for every single lesson
            if (visualizerBox) {
                visualizerBox.style.display = "block";
            }

            // 3. Initialize visualizer scripts and controls
            if (isCustomVisualizer) {
                initInteractiveVisualizer(cleanTitle);
            } else {
                initCategoryVisualizer(category);
            }

            // 4. Render MCQ Challenge (Use predefined or generate fallback)
            let challengeData = challenges[cleanTitle];
            if (!challengeData) {
                challengeData = defaultChallenges[category] || defaultChallenges["universal"];
            }

            if (challengeData && challengeBox) {
                challengePrompt.innerText = challengeData.prompt;
                if (challengeData.code) {
                    challengeCodeBox.innerText = challengeData.code;
                    challengeCodeBox.style.display = "block";
                } else {
                    challengeCodeBox.style.display = "none";
                }

                challengeChoices.innerHTML = "";
                challengeData.choices.forEach((choice, idx) => {
                    const btn = document.createElement("button");
                    btn.className = "choice-btn";
                    btn.innerText = choice;
                    btn.onclick = () => selectChoice(idx, challengeData.correct, challengeData.feedback);
                    challengeChoices.appendChild(btn);
                });

                challengeBox.style.display = "block";
            }
        });

        // Initialize general visualizer category parameters and sync
        function initCategoryVisualizer(category) {
            if (category === "neural") {
                const sLR = document.getElementById("s-lr");
                const sEpochs = document.getElementById("s-epochs");
                const sW1 = document.getElementById("s-w1");
                const sBias = document.getElementById("s-bias");

                const vLR = document.getElementById("v-lr");
                const vEpochs = document.getElementById("v-epochs");
                const vW1 = document.getElementById("v-w1");
                const vBias = document.getElementById("v-bias");

                const lblZ = document.getElementById("lbl-z");
                const lblA = document.getElementById("lbl-a");

                function updateNeuralCategory() {
                    const lr = parseFloat(sLR.value);
                    const epochs = parseInt(sEpochs.value);
                    const w1 = parseFloat(sW1.value);
                    const bias = parseFloat(sBias.value);

                    vLR.innerText = lr.toFixed(2);
                    vEpochs.innerText = epochs;
                    vW1.innerText = w1.toFixed(1);
                    vBias.innerText = bias.toFixed(1);

                    // Dynamic neuron math with standard x1=1.0, x2=0.5, w2=0.4
                    const x1 = 1.0, x2 = 0.5, w2 = 0.4;
                    const z = (x1 * w1) + (x2 * w2) + bias;
                    const a = 1 / (1 + Math.exp(-z));

                    lblZ.innerText = z.toFixed(2);
                    lblA.innerText = a.toFixed(2);

                    // Dynamically animate SVG nodes glowing based on parameters
                    document.getElementById("line-w1").style.opacity = (Math.max(0.1, Math.min(1, Math.abs(w1)))).toString();
                    document.getElementById("node-neuron").setAttribute("stroke-width", (Math.max(1, Math.min(5, Math.abs(z)*3))).toString());

                    // Sync parameters back into Python editor text
                    syncCodeEditor("neural", { lr, epochs, w1, bias });
                }

                if (sLR) {
                    [sLR, sEpochs, sW1, sBias].forEach(s => s.addEventListener("input", updateNeuralCategory));
                    updateNeuralCategory();
                }
            }

            if (category === "regression") {
                const sM = document.getElementById("s-m");
                const sB = document.getElementById("s-b");
                const sPts = document.getElementById("s-pts");
                const sNoise = document.getElementById("s-noise");

                const vM = document.getElementById("v-m");
                const vB = document.getElementById("v-b");
                const vPts = document.getElementById("v-pts");
                const vNoise = document.getElementById("v-noise");

                const lblMse = document.getElementById("lbl-mse");
                const lblR2 = document.getElementById("lbl-r2");
                const svg = document.getElementById("regression-svg");

                function updateRegressionCategory() {
                    const m = parseFloat(sM.value);
                    const b = parseFloat(sB.value);
                    const pts = parseInt(sPts.value);
                    const noise = parseFloat(sNoise.value);

                    vM.innerText = m.toFixed(1);
                    vB.innerText = b.toFixed(1);
                    vPts.innerText = pts;
                    vNoise.innerText = noise.toFixed(1);

                    // Calculate errors and coefficient
                    const mse = Math.max(1.5, Math.pow(noise, 2) * 0.25 + Math.abs(m * 2.5));
                    const r2 = Math.max(0.01, Math.min(0.99, 1 - (mse / 300)));

                    lblMse.innerText = mse.toFixed(1);
                    lblR2.innerText = r2.toFixed(2);

                    // Draw fit line and points inside SVG
                    svg.innerHTML = `
                        <line x1="20" y1="60" x2="380" y2="60" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
                        <line x1="200" y1="10" x2="200" y2="110" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
                    `;

                    // Generate pseudo points with noise
                    for (let i = 0; i < pts; i++) {
                        const px = 40 + (i * (320 / (pts - 1 || 1)));
                        const rawY = m * ((px - 200) / 30) + (b * 0.4);
                        const nVal = (Math.sin(i * 1.7) * noise * 0.6);
                        const py = Math.max(10, Math.min(110, 60 - rawY - nVal));

                        const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
                        dot.setAttribute("cx", px.toString());
                        dot.setAttribute("cy", py.toString());
                        dot.setAttribute("r", "3.5");
                        dot.setAttribute("fill", "var(--neon-purple)");
                        svg.appendChild(dot);
                    }

                    // Fit line path
                    const x1 = 20;
                    const y1 = Math.max(5, Math.min(115, 60 - (m * ((x1 - 200) / 30) + b * 0.4)));
                    const x2 = 380;
                    const y2 = Math.max(5, Math.min(115, 60 - (m * ((x2 - 200) / 30) + b * 0.4)));

                    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                    line.setAttribute("x1", x1.toString());
                    line.setAttribute("y1", y1.toString());
                    line.setAttribute("x2", x2.toString());
                    line.setAttribute("y2", y2.toString());
                    line.setAttribute("stroke", "#00ff80");
                    line.setAttribute("stroke-width", "2");
                    line.setAttribute("style", "filter: drop-shadow(0 0 4px #00ff80);");
                    svg.appendChild(line);

                    syncCodeEditor("regression", { m, b, pts, noise });
                }

                if (sM) {
                    [sM, sB, sPts, sNoise].forEach(s => s.addEventListener("input", updateRegressionCategory));
                    updateRegressionCategory();
                }
            }

            if (category === "genetic") {
                const sPop = document.getElementById("s-pop");
                const sGens = document.getElementById("s-gens");
                const sMut = document.getElementById("s-mut");
                const sCrossP = document.getElementById("s-crossp");

                const vPop = document.getElementById("v-pop");
                const vGens = document.getElementById("v-gens");
                const vMut = document.getElementById("v-mut");
                const vCrossP = document.getElementById("v-crossp");

                const c1 = document.getElementById("lbl-chrom1");
                const c2 = document.getElementById("lbl-chrom2");
                const cHijo = document.getElementById("lbl-chrom-hijo");

                function updateGeneticCategory() {
                    const pop = parseInt(sPop.value);
                    const gens = parseInt(sGens.value);
                    const mut = parseFloat(sMut.value);
                    const crossp = parseInt(sCrossP.value);

                    vPop.innerText = pop;
                    vGens.innerText = gens;
                    vMut.innerText = mut.toFixed(2);
                    vCrossP.innerText = crossp;

                    // Compute offspring
                    let str1 = "11111111".slice(0, crossp) + "00000000".slice(crossp);
                    let str2 = "00000000".slice(0, crossp) + "11111111".slice(crossp);

                    // Add simulated mutation at final bit
                    let finalHijo = str1.split("");
                    if (mut > 0.05) {
                        finalHijo[7] = finalHijo[7] === "1" ? "0" : "1";
                    }
                    finalHijo = finalHijo.join("");

                    cHijo.innerText = finalHijo;

                    syncCodeEditor("genetic", { pop, gens, mut, crossp });
                }

                if (sPop) {
                    [sPop, sGens, sMut, sCrossP].forEach(s => s.addEventListener("input", updateGeneticCategory));
                    updateGeneticCategory();
                }
            }

            if (category === "logic") {
                const sIn = document.getElementById("s-logic-in");
                const sTh = document.getElementById("s-logic-th");
                const vIn = document.getElementById("v-logic-in");
                const vTh = document.getElementById("v-logic-th");
                const badge = document.getElementById("logic-badge");

                function updateLogicCategory() {
                    const val = parseFloat(sIn.value);
                    const th = parseFloat(sTh.value);

                    vIn.innerText = val.toFixed(1);
                    vTh.innerText = th.toFixed(1);

                    if (val >= th) {
                        badge.innerText = "🟢 ACTIVA / ALERTA";
                        badge.style.background = "rgba(0, 255, 128, 0.15)";
                        badge.style.color = "#00ff80";
                        badge.style.border = "1px solid #00ff80";
                    } else {
                        badge.innerText = "🔴 INACTIVA / SEGURA";
                        badge.style.background = "rgba(255, 51, 51, 0.15)";
                        badge.style.color = "#ff3333";
                        badge.style.border = "1px solid #ff3333";
                    }

                    syncCodeEditor("logic", { val, th });
                }

                if (sIn) {
                    [sIn, sTh].forEach(s => s.addEventListener("input", updateLogicCategory));
                    updateLogicCategory();
                }
            }

            if (category === "swarm") {
                const sC1 = document.getElementById("s-c1");
                const sC2 = document.getElementById("s-c2");
                const sW = document.getElementById("s-w");

                const vC1 = document.getElementById("v-c1");
                const vC2 = document.getElementById("v-c2");
                const vW = document.getElementById("v-w");

                const lblVel = document.getElementById("lbl-swarm-vel");
                const lblConv = document.getElementById("lbl-swarm-conv");
                const svg = document.getElementById("swarm-svg");

                function updateSwarmCategory() {
                    const c1 = parseFloat(sC1.value);
                    const c2 = parseFloat(sC2.value);
                    const w = parseFloat(sW.value);

                    vC1.innerText = c1.toFixed(1);
                    vC2.innerText = c2.toFixed(1);
                    vW.innerText = w.toFixed(2);

                    const vel = Math.abs(w * 2.5 + (c1 - c2) * 0.4);
                    lblVel.innerText = vel.toFixed(2) + " m/s";

                    if (w <= 0.6 && c2 >= 2.0) {
                        lblConv.innerText = "CRÍTICA / RÁPIDA";
                        lblConv.style.color = "#00ff80";
                    } else if (w >= 1.2) {
                        lblConv.innerText = "DIVERGENTE / INESTABLE";
                        lblConv.style.color = "#ff3333";
                    } else {
                        lblConv.innerText = "CONVERGENCIA NORMAL";
                        lblConv.style.color = "var(--neon-blue)";
                    }

                    // Render animated particle paths in SVG
                    svg.innerHTML = `
                        <circle cx="200" cy="55" r="4" fill="#00ff80" style="filter: drop-shadow(0 0 3px #00ff80);"/>
                    `;

                    // Spawn small particle circles relative to parameters
                    for (let i = 0; i < 15; i++) {
                        const px = 200 + Math.sin(i * 1.5) * (w * 80) + (c1 - c2) * 8;
                        const py = 55 + Math.cos(i * 2.4) * (w * 40);

                        const p = document.createElementNS("http://www.w3.org/2000/svg", "circle");
                        p.setAttribute("cx", px.toString());
                        p.setAttribute("cy", py.toString());
                        p.setAttribute("r", "2");
                        p.setAttribute("fill", "var(--neon-blue)");
                        svg.appendChild(p);
                    }

                    syncCodeEditor("swarm", { c1, c2, w });
                }

                if (sC1) {
                    [sC1, sC2, sW].forEach(s => s.addEventListener("input", updateSwarmCategory));
                    updateSwarmCategory();
                }
            }

            if (category === "universal") {
                const sUA = document.getElementById("s-ua");
                const sUB = document.getElementById("s-ub");
                const vUA = document.getElementById("v-ua");
                const vUB = document.getElementById("v-ub");
                const lblVal = document.getElementById("lbl-uval");
                const svg = document.getElementById("universal-svg");

                function updateUniversalCategory() {
                    const ua = parseFloat(sUA.value);
                    const ub = parseFloat(sUB.value);

                    vUA.innerText = ua.toFixed(1);
                    vUB.innerText = ub.toFixed(1);

                    const finalResult = (ua * 10.0 + ub * 3.1416).toFixed(2);
                    lblVal.innerText = finalResult;

                    // Plot a beautiful dynamic trigonometric curve inside SVG
                    svg.innerHTML = `
                        <line x1="10" y1="55" x2="390" y2="55" stroke="rgba(255,255,255,0.05)"/>
                    `;

                    let pts = [];
                    for (let x = 0; x < 380; x += 4) {
                        const scaledX = (x / 380) * Math.PI * 6;
                        const waveVal = Math.sin(scaledX) * (ua * 4) + Math.cos(scaledX * 2) * (ub * 2);
                        const py = 55 - waveVal;
                        pts.push(\`\${x+10},\${py}\`);
                    }

                    const path = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
                    path.setAttribute("points", pts.join(" "));
                    path.setAttribute("fill", "none");
                    path.setAttribute("stroke", "var(--neon-blue)");
                    path.setAttribute("stroke-width", "1.5");
                    path.setAttribute("style", "filter: drop-shadow(0 0 3px var(--neon-blue));");
                    svg.appendChild(path);

                    syncCodeEditor("universal", { ua, ub });
                }

                if (sUA) {
                    [sUA, sUB].forEach(s => s.addEventListener("input", updateUniversalCategory));
                    updateUniversalCategory();
                }
            }
        }

        // Dynamically overwrite sandbox code blocks with new numbers
        function syncCodeEditor(category, params) {
            const editor = document.getElementById("code-sandbox-editor");
            if (!editor) return;

            let code = editor.value;

            if (category === "neural") {
                code = code.replace(/learning_rate\s*=\s*[\d\.]+/, `learning_rate = \${params.lr.toFixed(2)}`);
                code = code.replace(/epochs\s*=\s*\d+/, `epochs = \${params.epochs}`);
                code = code.replace(/w1\s*=\s*[\d\.-]+/, `w1 = \${params.w1.toFixed(1)}`);
                code = code.replace(/bias\s*=\s*[\d\.-]+/, `bias = \${params.bias.toFixed(1)}`);
            }
            else if (category === "regression") {
                code = code.replace(/slope_m\s*=\s*[\d\.-]+/, `slope_m = \${params.m.toFixed(1)}`);
                code = code.replace(/intercept_b\s*=\s*[\d\.-]+/, `intercept_b = \${params.b.toFixed(1)}`);
                code = code.replace(/data_points\s*=\s*\d+/, `data_points = \${params.pts}`);
                code = code.replace(/noise_level\s*=\s*[\d\.-]+/, `noise_level = \${params.noise.toFixed(1)}`);
            }
            else if (category === "genetic") {
                code = code.replace(/population_size\s*=\s*\d+/, `population_size = \${params.pop}`);
                code = code.replace(/generations\s*=\s*\d+/, `generations = \${params.gens}`);
                code = code.replace(/mutation_rate\s*=\s*[\d\.]+/, `mutation_rate = \${params.mut.toFixed(2)}`);
                code = code.replace(/crossover_point\s*=\s*\d+/, `crossover_point = \${params.crossp}`);
            }
            else if (category === "logic") {
                code = code.replace(/input_value\s*=\s*[\d\.-]+/, `input_value = \${params.val.toFixed(1)}`);
                code = code.replace(/threshold\s*=\s*[\d\.-]+/, `threshold = \${params.th.toFixed(1)}`);
            }
            else if (category === "swarm") {
                code = code.replace(/c1_cognitive\s*=\s*[\d\.-]+/, `c1_cognitive = \${params.c1.toFixed(1)}`);
                code = code.replace(/c2_social\s*=\s*[\d\.-]+/, `c2_social = \${params.c2.toFixed(1)}`);
                code = code.replace(/w_inertia\s*=\s*[\d\.-]+/, `w_inertia = \${params.w.toFixed(2)}`);
            }
            else if (category === "universal") {
                code = code.replace(/variable_a\s*=\s*[\d\.-]+/, `variable_a = \${params.ua.toFixed(1)}`);
                code = code.replace(/variable_b\s*=\s*[\d\.-]+/, `variable_b = \${params.ub.toFixed(1)}`);
            }

            editor.value = code;
        }

        // Run mock code sandbox interpreter inside browser
        window.runCodeSandbox = function() {
            const terminal = document.getElementById("code-sandbox-terminal");
            const indicator = document.getElementById("sandbox-running-indicator");
            const editorText = document.getElementById("code-sandbox-editor").value;

            if (!terminal) return;

            terminal.innerHTML = "";
            if (indicator) indicator.style.display = "inline";

            // Parse current parameters directly from editable python script text using simple regex
            let cleanTitle = lessonTitle.replace(/^\s*\[[A-Z]+\]\s*/, "");
            if (cleanTitle.includes("Introducción a la IA") || cleanTitle.includes("Historia de la IA")) {
                cleanTitle = "Historia de la IA";
            } else if (cleanTitle.includes("Test de Turing")) {
                cleanTitle = "Test de Turing";
            }
            const category = getLessonCategory(cleanTitle);

            let logs = [];
            logs.push(`Python Interpreter Active | CPython 3.14.0b1`);
            logs.push(`Running main.py inside virtual sandbox...\n`);

            setTimeout(() => {
                try {
                    if (category === "neural") {
                        const lrMatch = editorText.match(/learning_rate\s*=\s*([\d\.]+)/);
                        const epochsMatch = editorText.match(/epochs\s*=\s*(\d+)/);
                        const w1Match = editorText.match(/w1\s*=\s*([\d\.-]+)/);
                        const biasMatch = editorText.match(/bias\s*=\s*([\d\.-]+)/);

                        const lr = lrMatch ? parseFloat(lrMatch[1]) : 0.05;
                        const epochs = epochsMatch ? parseInt(epochsMatch[1]) : 100;
                        const w1 = w1Match ? parseFloat(w1Match[1]) : 0.8;
                        const bias = biasMatch ? parseFloat(biasMatch[1]) : -0.5;

                        // Sync sliders to edited code values
                        const sLR = document.getElementById("s-lr");
                        const sEpochs = document.getElementById("s-epochs");
                        const sW1 = document.getElementById("s-w1");
                        const sBias = document.getElementById("s-bias");

                        if (sLR) { sLR.value = lr; sEpochs.value = epochs; sW1.value = w1; sBias.value = bias; }

                        // Fire visual event in graph
                        const node = document.getElementById("node-neuron");
                        if (node) {
                            node.setAttribute("fill", "var(--neon-blue)");
                            setTimeout(() => node.setAttribute("fill", "#09090d"), 600);
                        }

                        // Generate logs
                        for (let e = 0; e <= epochs; e += Math.max(1, Math.floor(epochs / 4))) {
                            const loss = (0.5 / (1 + e * lr * 0.2)).toFixed(4);
                            const acc = (0.5 + 0.49 * (1 - 1/(1+e*lr*0.1))).toFixed(2);
                            logs.push(`[Época \${e}/\${epochs}] Loss: \${loss} | Prec: \${acc} | w1_grad: \${(w1*0.01).toFixed(4)}`);
                        }
                        logs.push(`\n🚀 Entrenamiento Neural completado con éxito. Pesos ajustados. Final Loss: \${(0.5 / (1 + epochs * lr * 0.2)).toFixed(4)}`);
                    }
                    else if (category === "regression") {
                        const mMatch = editorText.match(/slope_m\s*=\s*([\d\.-]+)/);
                        const bMatch = editorText.match(/intercept_b\s*=\s*([\d\.-]+)/);
                        const ptsMatch = editorText.match(/data_points\s*=\s*(\d+)/);
                        const noiseMatch = editorText.match(/noise_level\s*=\s*([\d\.-]+)/);

                        const m = mMatch ? parseFloat(mMatch[1]) : 1.5;
                        const b = bMatch ? parseFloat(bMatch[1]) : 10.0;
                        const pts = ptsMatch ? parseInt(ptsMatch[1]) : 15;
                        const noise = noiseMatch ? parseFloat(noiseMatch[1]) : 15.0;

                        const sM = document.getElementById("s-m");
                        const sB = document.getElementById("s-b");
                        const sPts = document.getElementById("s-pts");
                        const sNoise = document.getElementById("s-noise");

                        if (sM) { sM.value = m; sB.value = b; sPts.value = pts; sNoise.value = noise; }

                        const mse = Math.max(1.5, Math.pow(noise, 2) * 0.25 + Math.abs(m * 2.5));
                        const r2 = Math.max(0.01, Math.min(0.99, 1 - (mse / 300)));

                        logs.push(`Ajustando modelo de regresión lineal...`);
                        logs.push(`Número de muestras (N): \${pts} | Nivel de ruido: \${noise}`);
                        logs.push(`m óptima ajustada: \${m.toFixed(4)} | b óptima: \${b.toFixed(4)}`);
                        logs.push(`Error Cuadrático Medio final (MSE): \${mse.toFixed(2)}`);
                        logs.push(`Coeficiente de Determinación (R²): \${r2.toFixed(4)}`);
                    }
                    else if (category === "genetic") {
                        const popMatch = editorText.match(/population_size\s*=\s*(\d+)/);
                        const gensMatch = editorText.match(/generations\s*=\s*(\d+)/);
                        const mutMatch = editorText.match(/mutation_rate\s*=\s*([\d\.]+)/);
                        const crosspMatch = editorText.match(/crossover_point\s*=\s*(\d+)/);

                        const pop = popMatch ? parseInt(popMatch[1]) : 50;
                        const gens = gensMatch ? parseInt(gensMatch[1]) : 30;
                        const mut = mutMatch ? parseFloat(mutMatch[1]) : 0.1;
                        const crossp = crosspMatch ? parseInt(crosspMatch[1]) : 4;

                        const sPop = document.getElementById("s-pop");
                        const sGens = document.getElementById("s-gens");
                        const sMut = document.getElementById("s-mut");
                        const sCrossP = document.getElementById("s-crossp");

                        if (sPop) { sPop.value = pop; sGens.value = gens; sMut.value = mut; sCrossP.value = crossp; }

                        logs.push(`Creando población inicial aleatoria de \${pop} individuos...`);
                        for (let g = 0; g <= gens; g += Math.max(1, Math.floor(gens / 5))) {
                            const fit = (0.2 + 0.79 * (1 - 1/(1+g*mut*1.5))).toFixed(4);
                            logs.push(`Generación \${g}/\${gens} | Mutados: \${Math.floor(pop * mut)} | Max Fitness: \${fit}`);
                        }
                        logs.push(`\n🧬 Óptimo Genético alcanzado. Diversidad cromosómica preservada.`);
                    }
                    else if (category === "logic") {
                        const valMatch = editorText.match(/input_value\s*=\s*([\d\.-]+)/);
                        const thMatch = editorText.match(/threshold\s*=\s*([\d\.-]+)/);

                        const val = valMatch ? parseFloat(valMatch[1]) : 38.5;
                        const th = thMatch ? parseFloat(thMatch[1]) : 37.5;

                        const sIn = document.getElementById("s-logic-in");
                        const sTh = document.getElementById("s-logic-th");

                        if (sIn) { sIn.value = val; sTh.value = th; }

                        logs.push(`Evaluando motor de inferencia deductiva...`);
                        logs.push(`Entrada de Sensores: \${val} | Umbral de Activación: \${th}`);
                        if (val >= th) {
                            logs.push(`[REGLA DISPARADA]: IF (\${val} >= \${th}) -> DIAGNOSIS = ALERTA CRÍTICA`);
                        } else {
                            logs.push(`[REGLA CUMPLIDA]: IF (\${val} < \${th}) -> DIAGNOSIS = SISTEMA ESTABLE`);
                        }
                    }
                    else if (category === "swarm") {
                        const c1Match = editorText.match(/c1_cognitive\s*=\s*([\d\.-]+)/);
                        const c2Match = editorText.match(/c2_social\s*=\s*([\d\.-]+)/);
                        const wMatch = editorText.match(/w_inertia\s*=\s*([\d\.-]+)/);

                        const c1 = c1Match ? parseFloat(c1Match[1]) : 2.0;
                        const c2 = c2Match ? parseFloat(c2Match[1]) : 2.0;
                        const w = wMatch ? parseFloat(wMatch[1]) : 0.8;

                        const sC1 = document.getElementById("s-c1");
                        const sC2 = document.getElementById("s-c2");
                        const sW = document.getElementById("s-w");

                        if (sC1) { sC1.value = c1; sC2.value = c2; sW.value = w; }

                        logs.push(`Iniciando optimización por enjambre de partículas (PSO)...`);
                        logs.push(`Inercia w: \${w} | c1 cognitivo: \${c1} | c2 social: \${c2}`);
                        for (let i = 0; i <= 50; i += 10) {
                            const err = (10.0 / (1 + i * w * 0.4)).toFixed(4);
                            logs.push(`Iteración \${i}/50 | Mejor error global (gbest): \${err}`);
                        }
                        logs.push(`\n🪐 Enjambre convergido en el mínimo absoluto de la función.`);
                    }
                    else {
                        const uaMatch = editorText.match(/variable_a\s*=\s*([\d\.-]+)/);
                        const ubMatch = editorText.match(/variable_b\s*=\s*([\d\.-]+)/);

                        const ua = uaMatch ? parseFloat(uaMatch[1]) : 5.0;
                        const ub = ubMatch ? parseFloat(ubMatch[1]) : 2.5;

                        const sUA = document.getElementById("s-ua");
                        const sUB = document.getElementById("s-ub");

                        if (sUA) { sUA.value = ua; sUB.value = ub; }

                        const res = (ua * 10.0 + ub * 3.1416).toFixed(3);
                        logs.push(`Evaluando cálculo matricial general...`);
                        logs.push(`Variable A: \${ua} | Variable B: \${ub}`);
                        logs.push(`Resultado de la computación del modelo: \${res}`);
                    }
                } catch(err) {
                    logs.push(`[ERROR]: Excepción de sintaxis de Python: \${err.message}`);
                }

                // Inject logs into terminal console
                terminal.innerHTML = logs.join("\n");

                // Trigger update event to keep sliders and visual metrics fully synced
                if (category === "neural") {
                    const sLR = document.getElementById("s-lr");
                    if (sLR) sLR.dispatchEvent(new Event('input'));
                } else if (category === "regression") {
                    const sM = document.getElementById("s-m");
                    if (sM) sM.dispatchEvent(new Event('input'));
                } else if (category === "genetic") {
                    const sPop = document.getElementById("s-pop");
                    if (sPop) sPop.dispatchEvent(new Event('input'));
                } else if (category === "logic") {
                    const sIn = document.getElementById("s-logic-in");
                    if (sIn) sIn.dispatchEvent(new Event('input'));
                } else if (category === "swarm") {
                    const sC1 = document.getElementById("s-c1");
                    if (sC1) sC1.dispatchEvent(new Event('input'));
                } else {
                    const sUA = document.getElementById("s-ua");
                    if (sUA) sUA.dispatchEvent(new Event('input'));
                }

                if (indicator) indicator.style.display = "none";
            }, 600);
        };

        // Initialize interactive visualizer logic for specific custom lessons
        function initInteractiveVisualizer(title) {
            if (title === "Historia de la IA") {
                const slider = document.getElementById("timeline-slider");
                const label = document.getElementById("timeline-year-label");
                const card = document.getElementById("timeline-card");
                
                const milestones = [
                    { year: "1950", title: "El Juego de Imitación", text: "Alan Turing propone el famoso 'Test de Turing' para determinar si una máquina posee capacidad de pensar de manera indistinguible a un ser humano.", paradigm: "Paradigma Fundacional" },
                    { year: "1956", title: "Conferencia de Dartmouth", text: "John McCarthy, Marvin Minsky y Claude Shannon acuñan formalmente el término 'Inteligencia Artificial', marcando el nacimiento de la disciplina.", paradigm: "IA Simbólica (Clásica)" },
                    { year: "1974", title: "Primer Invierno de la IA", text: "Críticas matemáticas sobre las limitaciones del Perceptrón Simple de Rosenblatt para resolver problemas no lineales (como XOR) congelan el financiamiento.", paradigm: "Invierno e Incertidumbre" },
                    { year: "1997", title: "Deep Blue derrota a Kasparov", text: "La supercomputadora de IBM vence al campeón mundial de ajedrez en una partida histórica basada en fuerza bruta de cómputo y árboles de decisión.", paradigm: "Sistemas Expertos & Búsqueda" },
                    { year: "2026", title: "Modelos Cognitivos y LLMs", text: "Era de las Redes Neuronales Profundas (Deep Learning) masivas y agentes autónomos capaces de razonamiento emergente a partir de billones de parámetros.", paradigm: "IA Conexionista & Generativa" }
                ];
                
                function updateTimeline() {
                    const idx = parseInt(slider.value);
                    const m = milestones[idx];
                    label.innerText = m.year;
                    card.innerHTML = `
                        <div style="flex:1;">
                            <span style="font-size:0.65rem; background:rgba(0,242,255,0.15); color:var(--neon-blue); padding:0.2rem 0.5rem; border-radius:0.3rem; font-weight:800; text-transform:uppercase;">\${m.paradigm}</span>
                            <h4 style="margin:0.5rem 0 0.2rem 0; color:white; font-size:1rem; font-family:'Outfit';">\${m.title}</h4>
                            <p style="margin:0; font-size:0.8rem; color:rgba(255,255,255,0.7); line-height:1.4;">\${m.text}</p>
                        </div>
                    `;
                }
                
                if (slider) {
                    slider.addEventListener("input", updateTimeline);
                    updateTimeline();
                }
            }
            
            if (title === "Test de Turing") {
                const input = document.getElementById("chat-input");
                const sendBtn = document.getElementById("chat-send-btn");
                const messages = document.getElementById("chat-messages");
                
                function handleSend() {
                    const text = input.value.trim();
                    if (!text) return;
                    
                    // Add user message
                    const uMsg = document.createElement("div");
                    uMsg.style.color = "white";
                    uMsg.style.marginBottom = "0.3rem";
                    uMsg.innerHTML = \`<strong>[Tú]:</strong> \${text}\`;
                    messages.appendChild(uMsg);
                    input.value = "";
                    messages.scrollTop = messages.scrollHeight;
                    
                    // Respond after delay
                    setTimeout(() => {
                        const lowText = text.toLowerCase();
                        let reply = "Es una buena pregunta. Depende de cómo lo veas, a veces los humanos actuamos de forma muy predecible.";
                        if (lowText.includes("hola") || lowText.includes("quien")) {
                            reply = "Soy una persona común que vive en Bogotá, me gusta el café y leer libros de ciencia ficción.";
                        } else if (lowText.includes("calcula") || lowText.includes("matematica") || lowText.includes("raiz")) {
                            reply = "Un segundo... la verdad es que odio las matemáticas, déjame buscar una calculadora en mi celular.";
                        } else if (lowText.includes("turing") || lowText.includes("robot") || lowText.includes("inteligencia")) {
                            reply = "Jaja, ¿de verdad crees que soy un robot? Esa es una pregunta capciosa...";
                        }
                        
                        const rMsg = document.createElement("div");
                        rMsg.style.color = "#ffaa00";
                        rMsg.style.marginBottom = "0.3rem";
                        rMsg.innerHTML = \`<strong>[Interlocutor]:</strong> \${reply}\`;
                        messages.appendChild(rMsg);
                        messages.scrollTop = messages.scrollHeight;
                    }, 800);
                }
                
                if (sendBtn && input) {
                    sendBtn.addEventListener("click", handleSend);
                    input.addEventListener("keypress", (e) => {
                        if (e.key === "Enter") handleSend();
                    });
                }
            }
            
            if (title === "Tu Primera Neurona") {
                const sX1 = document.getElementById("slide-x1");
                const sX2 = document.getElementById("slide-x2");
                const sW1 = document.getElementById("slide-w1");
                const sW2 = document.getElementById("slide-w2");
                const sBias = document.getElementById("slide-bias");
                
                const vX1 = document.getElementById("val-x1");
                const vX2 = document.getElementById("val-x2");
                const vW1 = document.getElementById("val-w1");
                const vW2 = document.getElementById("val-w2");
                const vBias = document.getElementById("val-bias");
                
                const cZ = document.getElementById("calc-z");
                const cA = document.getElementById("calc-a");
                const badge = document.getElementById("neuron-fire-badge");
                
                function updateNeuron() {
                    const x1 = parseFloat(sX1.value);
                    const x2 = parseFloat(sX2.value);
                    const w1 = parseFloat(sW1.value);
                    const w2 = parseFloat(sW2.value);
                    const bias = parseFloat(sBias.value);
                    
                    vX1.innerText = x1.toFixed(1);
                    vX2.innerText = x2.toFixed(1);
                    vW1.innerText = w1.toFixed(1);
                    vW2.innerText = w2.toFixed(1);
                    vBias.innerText = bias.toFixed(1);
                    
                    const z = (x1 * w1) + (x2 * w2) + bias;
                    const a = 1 / (1 + Math.exp(-z));
                    
                    cZ.innerText = z.toFixed(2);
                    cA.innerText = a.toFixed(2);
                    
                    if (a >= 0.5) {
                        badge.innerText = "🟢 ACTIVADA / APRUEBA";
                        badge.style.background = "rgba(0, 255, 128, 0.15)";
                        badge.style.color = "#00ff80";
                        badge.style.border = "1px solid #00ff80";
                    } else {
                        badge.innerText = "🔴 INACTIVA / RECHAZA";
                        badge.style.background = "rgba(255, 51, 51, 0.15)";
                        badge.style.color = "#ff3333";
                        badge.style.border = "1px solid #ff3333";
                    }
                }
                
                if (sX1) {
                    [sX1, sX2, sW1, sW2, sBias].forEach(s => s.addEventListener("input", updateNeuron));
                    updateNeuron();
                }
            }
            
            if (title === "Estadística Predictiva") {
                const input = document.getElementById("stats-input-data");
                const btn = document.getElementById("stats-calc-btn");
                const mVal = document.getElementById("stats-mean");
                const vVal = document.getElementById("stats-variance");
                const sVal = document.getElementById("stats-stddev");
                const canvas = document.getElementById("stats-chart-canvas");
                
                function calculateStats() {
                    const raw = input.value.split(",").map(n => parseFloat(n.trim())).filter(n => !isNaN(n));
                    if (raw.length === 0) return;
                    
                    const sum = raw.reduce((a, b) => a + b, 0);
                    const mean = sum / raw.length;
                    
                    const sqDiffSum = raw.reduce((a, b) => a + Math.pow(b - mean, 2), 0);
                    const variance = sqDiffSum / raw.length;
                    const stdDev = Math.sqrt(variance);
                    
                    mVal.innerText = mean.toFixed(1);
                    vVal.innerText = variance.toFixed(1);
                    sVal.innerText = stdDev.toFixed(1);
                    
                    // Render chart
                    const max = Math.max(...raw, mean) || 1;
                    const min = 0;
                    
                    canvas.innerHTML = "";
                    
                    // Mean line
                    const meanPct = ((mean - min) / (max - min)) * 80;
                    const line = document.createElement("div");
                    line.style.position = "absolute";
                    line.style.bottom = `\${meanPct}%`;
                    line.style.left = "0";
                    line.style.width = "100%";
                    line.style.borderBottom = "2px dashed var(--neon-blue)";
                    line.style.zIndex = "2";
                    line.innerHTML = \`<span style="font-size:0.6rem; color:var(--neon-blue); background:#050505; padding:0.1rem 0.3rem; border-radius:0.2rem; position:absolute; right:5px; bottom:2px;">MEDIA: \${mean.toFixed(1)}</span>\`;
                    canvas.appendChild(line);
                    
                    // Bars
                    const container = document.createElement("div");
                    container.style.display = "flex";
                    container.style.justifyContent = "space-around";
                    container.style.alignItems = "flex-end";
                    container.style.height = "100%";
                    container.style.padding = "0 1rem";
                    
                    raw.forEach(val => {
                        const pct = ((val - min) / (max - min)) * 80;
                        const bar = document.createElement("div");
                        bar.style.width = `\${Math.max(15, 60 / raw.length)}%`;
                        bar.style.height = `\${pct}%`;
                        bar.style.background = "linear-gradient(to top, var(--neon-purple), #ff00e6)";
                        bar.style.borderRadius = "0.3rem 0.3rem 0 0";
                        bar.style.position = "relative";
                        bar.style.textAlign = "center";
                        bar.innerHTML = \`<span style="font-size:0.65rem; color:white; position:absolute; top:-15px; left:50%; transform:translateX(-50%); font-weight:bold;">\${val}</span>\`;
                        container.appendChild(bar);
                    });
                    
                    canvas.appendChild(container);
                }
                
                if (btn) {
                    btn.addEventListener("click", calculateStats);
                    calculateStats();
                }
            }
            
            if (title === "Variables Dummy") {
                const s1 = document.getElementById("dummy-e1");
                const s2 = document.getElementById("dummy-e2");
                const s3 = document.getElementById("dummy-e3");
                const body = document.getElementById("dummy-matrix-body");
                
                function updateDummy() {
                    const choices = [s1.value, s2.value, s3.value];
                    body.innerHTML = "";
                    
                    choices.forEach((choice, idx) => {
                        const cellBog = choice === "Bogotá" ? "<span style='color:#00ff80; font-weight:bold;'>1</span>" : "<span style='color:rgba(255,255,255,0.2);'>0</span>";
                        const cellCal = choice === "Cali" ? "<span style='color:#00ff80; font-weight:bold;'>1</span>" : "<span style='color:rgba(255,255,255,0.2);'>0</span>";
                        const cellMed = choice === "Medellín" ? "<span style='color:#00ff80; font-weight:bold;'>1</span>" : "<span style='color:rgba(255,255,255,0.2);'>0</span>";
                        
                        const tr = document.createElement("tr");
                        tr.style.borderBottom = "1px solid rgba(255,255,255,0.05)";
                        tr.innerHTML = `
                            <td style="padding:0.6rem; text-align:left; color:white; font-weight:bold;">Estudiante \${idx+1} (\${choice})</td>
                            <td style="padding:0.6rem; background:\${choice === 'Bogotá' ? 'rgba(0,255,128,0.05)' : 'transparent'};">\${cellBog}</td>
                            <td style="padding:0.6rem; background:\${choice === 'Cali' ? 'rgba(0,255,128,0.05)' : 'transparent'};">\${cellCal}</td>
                            <td style="padding:0.6rem; background:\${choice === 'Medellín' ? 'rgba(0,255,128,0.05)' : 'transparent'};">\${cellMed}</td>
                        `;
                        body.appendChild(tr);
                    });
                }
                
                if (s1) {
                    [s1, s2, s3].forEach(s => s.addEventListener("change", updateDummy));
                    updateDummy();
                }
            }
            
            if (title === "Regresión Logística") {
                const sZ = document.getElementById("slide-log-z");
                const sTh = document.getElementById("slide-log-threshold");
                const vZ = document.getElementById("val-log-z");
                const vTh = document.getElementById("val-log-threshold");
                const pVal = document.getElementById("log-prob");
                const badge = document.getElementById("log-class-badge");
                const svg = document.getElementById("sigmoid-svg");
                
                function updateLogistic() {
                    const z = parseFloat(sZ.value);
                    const threshold = parseFloat(sTh.value);
                    
                    vZ.innerText = z.toFixed(1);
                    vTh.innerText = threshold.toFixed(2);
                    
                    const prob = 1 / (1 + Math.exp(-z));
                    pVal.innerText = \`\${(prob * 100).toFixed(1)}%\`;
                    
                    const isClass1 = prob >= threshold;
                    if (isClass1) {
                        badge.innerText = "CLASE: 1 (APROBADO)";
                        badge.style.background = "rgba(0, 255, 128, 0.15)";
                        badge.style.color = "#00ff80";
                        badge.style.border = "1px solid #00ff80";
                    } else {
                        badge.innerText = "CLASE: 0 (RECHAZADO)";
                        badge.style.background = "rgba(255, 51, 51, 0.15)";
                        badge.style.color = "#ff3333";
                        badge.style.border = "1px solid #ff3333";
                    }
                    
                    // Draw Sigmoid plot inside SVG
                    svg.innerHTML = `
                        <!-- X & Y Axes -->
                        <line x1="20" y1="65" x2="280" y2="65" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
                        <line x1="150" y1="10" x2="150" y2="120" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
                        
                        <!-- Grid lines -->
                        <line x1="20" y1="15" x2="280" y2="15" stroke="rgba(255,255,255,0.03)" stroke-width="1" stroke-dasharray="2,2"/>
                        <line x1="20" y1="115" x2="280" y2="115" stroke="rgba(255,255,255,0.03)" stroke-width="1" stroke-dasharray="2,2"/>
                        
                        <!-- Labels -->
                        <text x="285" y="68" fill="rgba(255,255,255,0.3)" font-size="7">z</text>
                        <text x="155" y="15" fill="rgba(255,255,255,0.3)" font-size="7">y</text>
                        <text x="10" y="18" fill="rgba(255,255,255,0.3)" font-size="7">1.0</text>
                        <text x="10" y="118" fill="rgba(255,255,255,0.3)" font-size="7">0.0</text>
                    `;
                    
                    // Sigmoid curve path
                    let points = [];
                    for (let x = -6; x <= 6; x += 0.2) {
                        const px = 150 + (x * 20); // Scale x from [-6, 6] to [30, 270]
                        const pyVal = 1 / (1 + Math.exp(-x));
                        const py = 115 - (pyVal * 100); // Scale y from [0, 1] to [115, 15]
                        points.push(\`\${px},\${py}\`);
                    }
                    
                    const path = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
                    path.setAttribute("points", points.join(" "));
                    path.setAttribute("fill", "none");
                    path.setAttribute("stroke", "rgba(0, 242, 255, 0.4)");
                    path.setAttribute("stroke-width", "2");
                    svg.appendChild(path);
                    
                    // Threshold horizontal line
                    const thY = 115 - (threshold * 100);
                    const thLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
                    thLine.setAttribute("x1", "20");
                    thLine.setAttribute("y1", thY.toString());
                    thLine.setAttribute("x2", "280");
                    thLine.setAttribute("y2", thY.toString());
                    thLine.setAttribute("stroke", "rgba(188, 19, 254, 0.5)");
                    thLine.setAttribute("stroke-width", "1");
                    thLine.setAttribute("stroke-dasharray", "4,3");
                    svg.appendChild(thLine);
                    
                    // Current dot on curve
                    const dotX = 150 + (z * 20);
                    const dotY = 115 - (prob * 100);
                    
                    const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
                    dot.setAttribute("cx", dotX.toString());
                    dot.setAttribute("cy", dotY.toString());
                    dot.setAttribute("r", "5");
                    dot.setAttribute("fill", isClass1 ? "#00ff80" : "#ff3333");
                    dot.setAttribute("style", "filter: drop-shadow(0 0 4px " + (isClass1 ? "#00ff80" : "#ff3333") + ");");
                    svg.appendChild(dot);
                }
                
                if (sZ) {
                    sZ.addEventListener("input", updateLogistic);
                    sTh.addEventListener("input", updateLogistic);
                    updateLogistic();
                }
            }
            
            if (title === "Cruce (Crossover)") {
                const s1 = document.getElementById("cross-p1");
                const s2 = document.getElementById("cross-p2");
                const sPoint = document.getElementById("slide-cross-point");
                const vPoint = document.getElementById("val-cross-point");
                
                const visP1 = document.getElementById("cross-vis-p1");
                const visP2 = document.getElementById("cross-vis-p2");
                const visHijo = document.getElementById("cross-vis-hijo");
                
                function updateCrossover() {
                    const p1 = s1.value.trim();
                    const p2 = s2.value.trim();
                    const point = parseInt(sPoint.value);
                    
                    vPoint.innerText = point;
                    
                    const len = Math.max(p1.length, p2.length, 8);
                    sPoint.max = len - 1;
                    
                    let p1Str = p1.padEnd(len, "1");
                    let p2Str = p2.padEnd(len, "0");
                    
                    const p1Left = p1Str.slice(0, point);
                    const p1Right = p1Str.slice(point);
                    const p2Left = p2Str.slice(0, point);
                    const p2Right = p2Str.slice(point);
                    
                    visP1.innerHTML = \`<span style="color:var(--neon-blue); font-weight:bold;">\${p1Left}</span><span style="color:rgba(255,255,255,0.4);">\${p1Right}</span>\`;
                    visP2.innerHTML = \`<span style="color:rgba(255,255,255,0.4);">\${p2Left}</span><span style="color:var(--neon-purple); font-weight:bold;">\${p2Right}</span>\`;
                    visHijo.innerHTML = \`<span style="color:var(--neon-blue); text-shadow:0 0 10px var(--neon-blue); font-weight:bold;">\${p1Left}</span><span style="color:var(--neon-purple); text-shadow:0 0 10px var(--neon-purple); font-weight:bold;">\${p2Right}</span>\`;
                }
                
                if (sPoint) {
                    [s1, s2].forEach(s => s.addEventListener("input", updateCrossover));
                    sPoint.addEventListener("input", updateCrossover);
                    updateCrossover();
                }
            }
            
            if (title === "Mutación") {
                const input = document.getElementById("mut-indiv");
                const btn = document.getElementById("mut-random-btn");
                const sIdx = document.getElementById("slide-mut-index");
                const vIdx = document.getElementById("val-mut-index");
                
                const visOrig = document.getElementById("mut-vis-orig");
                const visMut = document.getElementById("mut-vis-mut");
                
                function updateMutation() {
                    const raw = input.value.trim().padEnd(8, "0").slice(0, 12);
                    const idx = parseInt(sIdx.value);
                    
                    sIdx.max = raw.length - 1;
                    vIdx.innerText = idx;
                    
                    let mutated = raw.split("");
                    mutated[idx] = mutated[idx] === "1" ? "0" : "1";
                    mutated = mutated.join("");
                    
                    let origHtml = "";
                    let mutHtml = "";
                    
                    for (let i = 0; i < raw.length; i++) {
                        if (i === idx) {
                            origHtml += \`<span style="color:#ff3333; font-weight:bold; border:1px solid rgba(255,51,51,0.3); padding:0 3px; border-radius:3px;">\${raw[i]}</span>\`;
                            mutHtml += \`<span style="color:#00ff80; font-weight:bold; border:1px solid rgba(0,255,128,0.5); padding:0 3px; border-radius:3px; text-shadow:0 0 8px #00ff80;">\${mutated[i]}</span>\`;
                        } else {
                            origHtml += \`<span style="color:rgba(255,255,255,0.75);">\${raw[i]}</span>\`;
                            mutHtml += \`<span style="color:rgba(255,255,255,0.75);">\${mutated[i]}</span>\`;
                        }
                    }
                    
                    visOrig.innerHTML = origHtml;
                    visMut.innerHTML = mutHtml;
                }
                
                if (sIdx) {
                    input.addEventListener("input", updateMutation);
                    sIdx.addEventListener("input", updateMutation);
                    btn.addEventListener("click", () => {
                        const rand = Math.floor(Math.random() * input.value.trim().length);
                        sIdx.value = rand;
                        updateMutation();
                    });
                    updateMutation();
                }
            }
        }

        // Global function for Turing Test verdict
        window.judgeTuring = function(choice) {
            const verdict = document.getElementById("turing-verdict");
            if (!verdict) return;
            
            verdict.style.display = "block";
            if (choice === "maquina") {
                verdict.style.color = "#00ff80";
                verdict.style.borderColor = "rgba(0, 255, 128, 0.2)";
                verdict.style.background = "rgba(0, 255, 128, 0.05)";
                verdict.innerHTML = "🟢 ¡CORRECTO! El interlocutor era efectivamente un programa inteligente ejecutando un script de conversación en Javascript.";
            } else {
                verdict.style.color = "#ff3333";
                verdict.style.borderColor = "rgba(255, 51, 51, 0.2)";
                verdict.style.background = "rgba(255, 51, 51, 0.05)";
                verdict.innerHTML = "🔴 ¡TE HA ENGAÑADO! El interlocutor logró imitar exitosamente respuestas conversacionales humanas usando reglas condicionales.";
            }
        };

        function selectChoice(selectedIndex, correctIndex, feedbackText) {
            const choicesContainer = document.getElementById("challengeChoices");
            const feedbackDiv = document.getElementById("challengeFeedback");
            const buttons = choicesContainer.getElementsByClassName("choice-btn");

            // Disable all choices to avoid double clicking
            for (let i = 0; i < buttons.length; i++) {
                buttons[i].disabled = true;
                buttons[i].classList.remove("correct-choice", "wrong-choice");

                if (i === correctIndex) {
                    buttons[i].classList.add("correct-choice");
                } else if (i === selectedIndex) {
                    buttons[i].classList.add("wrong-choice");
                }
            }

            // Show feedback
            if (feedbackDiv) {
                feedbackDiv.style.display = "block";
                if (selectedIndex === correctIndex) {
                    feedbackDiv.style.background = "rgba(0, 255, 128, 0.1)";
                    feedbackDiv.style.border = "1px solid #00ff80";
                    feedbackDiv.style.color = "#00ff80";
                    feedbackDiv.innerHTML = `<strong>🟢 ¡PROTOCOLO DE COMPRENSIÓN EXITOSO!</strong><br>\${feedbackText}`;
                } else {
                    feedbackDiv.style.background = "rgba(255, 51, 51, 0.1)";
                    feedbackDiv.style.border = "1px solid #ff3333";
                    feedbackDiv.style.color = "#ff3333";
                    feedbackDiv.innerHTML = `<strong>🔴 INCONSISTENCIA DE MEMORIA DETECTADA</strong><br>Opción incorrecta. Repasa el diagrama e inténtalo de nuevo.<br><br><em>Explicación:</em> \${feedbackText}`;

                    // Allow retry after 1.8 seconds by enabling buttons again
                    setTimeout(() => {
                        for (let i = 0; i < buttons.length; i++) {
                            buttons[i].disabled = false;
                            buttons[i].classList.remove("correct-choice", "wrong-choice");
                        }
                        feedbackDiv.style.display = "none";
                    }, 1800);
                }
            }
        }
    