from common.analysis import CommunityAnalysis
from common.globals import *

class CommunityBenchmark:
    def __init__(self, file_path=None, graph=None, sep="\t", directed=False, iterations=100):
        self.file_path = file_path
        self.graph = graph
        self.sep = sep
        self.directed = directed
        self.iterations = iterations
        self.results = []

    def run(self):

        for i in range(self.iterations):
            print(f"Running iteration {i + 1}/{self.iterations} ...")
            ca = CommunityAnalysis(graph=self.graph)
            result = ca.run()
            self.results.append(result)

        self.df = pd.concat(self.results, ignore_index=True)
        return self.df

    def summarize(self):
        df_summary = self.df.groupby("Method").agg(["mean", "std", "min", "max"])
        df_summary.columns = ["_".join(col) for col in df_summary.columns]
        self.df_summary = df_summary
        self.df_summary.to_csv("community_detection_statistics_per_method.csv")
        print(self.df_summary)
        return self.df_summary

    def plot_violin(self, metric, title=None, ylabel=None, save_as=None, logscale=False):
        plt.figure(figsize=(12, 6))
        sns.violinplot(data=self.df, x="Method", y=metric, palette="Set2")
        plt.xlabel("Algorithm")
        plt.ylabel(ylabel or metric)
        plt.title(title or f"Distribution of {metric} across methods")
        plt.xticks(rotation=45)
        if logscale:
            plt.yscale("log")
        if save_as:
            plt.savefig(save_as, dpi=300, bbox_inches="tight")
        else:
            plt.show()

    def plot_all(self):
        plots = [
            ("Num Communities", "Number of detected communities", "num_communities.jpg"),
            ("Max Size", "Size of the largest community", "max_size.jpg"),
            ("Avg Size", "Average community size", "avg_size.jpg"),
            ("Modularity", "Modularity comparison", "modularity.jpg"),
            ("Avg. density:", "Average density", "avg_density.jpg"),
            ("Avg. degree:", "Average degree", "avg_degree.jpg"),
            ("Avg. clustering:", "Clustering coefficient", "avg_clustering.jpg"),
            ("Execution Time (s)", "Execution time", "exec_time.jpg", True),
        ]
        for metric, title, filename, *log in plots:
            self.plot_violin(metric, title=title, ylabel=title, save_as=filename, logscale=log[0] if log else False)