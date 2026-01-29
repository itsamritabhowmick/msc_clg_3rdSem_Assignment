# Write a Python Program to create target string ("Computer Science"), starting from random string using genetic algorithm. 

import random
def generate_random_string(length):
    return ''.join(
        random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.;:_!\"#%&/()=?@${[]}"
        )
        for _ in range(length)
    )


def calculate_fitness(candidate, target):
    return sum(1 for a, b in zip(candidate, target) if a == b)


def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]


def mutate(child, mutation_rate):
    return ''.join(
        c if random.random() > mutation_rate else random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.-;:_!\"#%&/()=?@${[]}"
        )
        for c in child
    )


def genetic_algorithm(
    target,
    population_size,
    mutation_rate,
    max_generations,
    elite_size=2
):
    population = [
        generate_random_string(len(target))
        for _ in range(population_size)
    ]

    for generation in range(max_generations):

        # Evaluate fitness
        fitness_scores = [
            calculate_fitness(candidate, target)
            for candidate in population
        ]

        # Select elites
        elites_indices = sorted(
            range(population_size),
            key=lambda i: fitness_scores[i],
            reverse=True
        )[:elite_size]

        elites = [population[i] for i in elites_indices]

        # Parent selection (roulette wheel)
        parents = random.choices(
            population,
            weights=fitness_scores,
            k=population_size - elite_size
        )

        # Create next generation
        next_generation = elites[:]
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            next_generation.append(child)

        population = next_generation

        # Best candidate
        best_candidate_index = max(
            range(population_size),
            key=lambda i: fitness_scores[i]
        )
        best_candidate = population[best_candidate_index]

        print(
            f"Generation {generation + 1}: "
            f"Best Candidate - {best_candidate}, "
            f"Fitness - {fitness_scores[best_candidate_index]}"
        )

        # Check termination condition
        if calculate_fitness(best_candidate, target) == len(target):
            print(f"Target reached in generation {generation + 1}!")
            break


if __name__ == "__main__":
    target_string = "Computer Science"

    print("\nRunning with smaller population:")
    genetic_algorithm(
        target_string,
        population_size=20,
        mutation_rate=0.02,
        max_generations=25
    )
