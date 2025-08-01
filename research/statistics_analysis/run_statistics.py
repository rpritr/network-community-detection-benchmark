from common.imports import *
from common.globals import *

# set number of iterations
num_iterations = 100

# results array
all_results = []
#G = nx.karate_club_graph()

# run analysis
for i in range(num_iterations):
    print(f"Izvajam iteracijo {i + 1}/{num_iterations} ...")
    #results = network_analysis(G, None)
    #results = network_analysis(None, "../../data/neuro/average_connectivity_condition_1.txt", " ")
    #results = network_analysis(None, "../../data/FakeNews-2010_Retweets_Graph.txt")
    results = network_analysis(None, "../../data/eu/email-EuAll.txt", directed=True)
    #results = network_analysis(None, "../../data/citation/cit-Patents.txt")

    all_results.append(results)

# combine into Dataframe
df_results = pd.concat(all_results, ignore_index=True)

# group results by method
stats_per_method = df_results.groupby("Method").agg(["mean", "std", "min", "max"])

# save results
pd.set_option('display.max_columns', None)

print(stats_per_method)
stats_per_method.columns = ["_".join(col) for col in stats_per_method.columns]
stats_per_method.to_csv("community_detection_statistics_per_method.csv")


# plot violin chart - communities by number of comunities
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_results, x="Method", y="Num Communities", palette="Set2")
plt.xlabel("Algoritem")  # Lastno ime za x-os
plt.ylabel("Število zaznanih skupnosti")  #
plt.title("Primerjava skupnosti med algoritmi")
plt.xticks(rotation=45)
plt.savefig("num_communities.jpg", dpi=300, bbox_inches="tight")

#plt.show()

# plot violin chart - communities : biggest community siye
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_results, x="Method", y="Max Size", palette="Set2")
plt.xlabel("Algoritem")  # Lastno ime za x-os
plt.ylabel("Velikost največje skupnosti")  #
plt.title("Primerjava največje skupnosti med algoritmi")
plt.xticks(rotation=45)
plt.savefig("max_size.jpg", dpi=300, bbox_inches="tight")

# plot violin chart - communities : number of average community size
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_results, x="Method", y="Avg Size", palette="Set2")
plt.xlabel("Algoritem")  # Lastno ime za x-os
plt.ylabel("Povprečna velikost skupnosti")  #
plt.title("Primerjava velikosti skupnosti med algoritmi")
plt.xticks(rotation=45)
plt.savefig("avg_size.jpg", dpi=300, bbox_inches="tight")

# plot violin chart - communities : number of modularity
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_results, x="Method", y="Modularity", palette="Set2")
plt.title("Primerjava modularnosti med algoritmi")
plt.xlabel("Algoritem")  # Lastno ime za x-os
plt.ylabel("Modularnost")  #
plt.xticks(rotation=45)
plt.savefig("modularity.jpg", dpi=300, bbox_inches="tight")

# plot violin chart - communities : number of average density
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_results, x="Method", y="Avg. density:", palette="Set2")
plt.xlabel("Algoritem")  # Lastno ime za x-os
plt.ylabel("Povprečna gostota")  #
plt.title("Primerjava gostote med algoritmi")
plt.xticks(rotation=45)
plt.savefig("avg_density.jpg", dpi=300, bbox_inches="tight")

# plot violin chart - communities : number of average degree
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_results, x="Method", y="Avg. degree:", palette="Set2")
plt.xlabel("Algoritem")  # Lastno ime za x-os
plt.ylabel("Povprečna stopnja")  #
plt.title("Primerjava povprečne stopnje med algoritmi")
plt.xticks(rotation=45)
plt.savefig("avg_degree.jpg", dpi=300, bbox_inches="tight")

# plot violin chart - communities : number of average clustering
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_results, x="Method", y="Avg. clustering:", palette="pastel")
plt.title("Porazdelitev povprečnega koeficienta gručenja med algoritmi")
plt.xlabel("Algoritem")  # Lastno ime za x-os
plt.ylabel("Koeficient gručenja")  #
plt.xticks(rotation=45)
plt.savefig("avg_clustering.jpg", dpi=300, bbox_inches="tight")






# 4️⃣ Boxplot - analiza izvajalnega časa
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_results, x="Method", y="Execution Time (s)", palette="muted")
plt.title("Primerjava časa izvajanja med algoritmi")
plt.xlabel("Algoritem")  # Lastno ime za x-os
plt.ylabel("Čas izvajanja (s)")  #
plt.xticks(rotation=45)
plt.yscale("log")  # Log skala zaradi velikih razlik v času izvajanja
plt.savefig("exec_time.jpg", dpi=300, bbox_inches="tight")

