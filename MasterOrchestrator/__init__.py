
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    input_data = yield context.call_activity("GetInputDataFn", None)

    map_results = yield context.task_all(
        [context.call_activity("Mapper", line) for line in input_data]
    )

    shuffled_data = yield context.call_activity("Shuffler", map_results)

    reduce_results = yield context.task_all(
        [context.call_activity("Reducer", (word, counts)) for word, counts in shuffled_data.items()]
    )

    return reduce_results

main = df.Orchestrator.create(orchestrator_function)
