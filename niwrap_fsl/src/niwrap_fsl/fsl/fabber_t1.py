# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FABBER_T1_METADATA = Metadata(
    id="ce3c716e36f55f0aa97d6ec169e5de17639579d4.boutiques",
    name="fabber_t1",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FabberT1Parameters = typing.TypedDict('FabberT1Parameters', {
    "__STYXTYPE__": typing.Literal["fabber_t1"],
    "output": str,
    "method": str,
    "model": str,
    "data": InputPathType,
    "data_mult": typing.NotRequired[list[InputPathType] | None],
    "data_order": typing.NotRequired[str | None],
    "mask": typing.NotRequired[InputPathType | None],
    "masked_time_points": typing.NotRequired[list[float] | None],
    "supp_data": typing.NotRequired[InputPathType | None],
    "overwrite": bool,
    "link_to_latest": bool,
    "simple_output": bool,
    "load_models": typing.NotRequired[InputPathType | None],
    "evaluate": typing.NotRequired[str | None],
    "evaluate_params": typing.NotRequired[str | None],
    "evaluate_nt": typing.NotRequired[float | None],
    "dump_param_names": bool,
    "save_model_fit": bool,
    "save_residuals": bool,
    "save_model_extras": bool,
    "save_mvn": bool,
    "save_mean": bool,
    "save_std": bool,
    "save_var": bool,
    "save_zstat": bool,
    "save_noise_mean": bool,
    "save_noise_std": bool,
    "save_free_energy": bool,
    "optfile": typing.NotRequired[InputPathType | None],
    "debug": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "fabber_t1": fabber_t1_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "fabber_t1": fabber_t1_outputs,
    }.get(t)


class FabberT1Outputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber_t1(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    param_names: OutputPathType
    """File containing the names of the model parameters"""
    model_fit: OutputPathType
    """Output the model prediction as a 4D volume"""
    residuals: OutputPathType
    """Output the residuals (difference between the data and the model
    prediction)"""
    model_extras: OutputPathType
    """Output any additional model-specific timeseries data"""
    mvn_distributions: OutputPathType
    """Output the final MVN distributions"""
    param_means: OutputPathType
    """Output the parameter means"""
    param_stds: OutputPathType
    """Output the parameter standard deviations"""
    param_vars: OutputPathType
    """Output the parameter variances"""
    param_zstats: OutputPathType
    """Output the parameter Z-stats"""
    noise_means: OutputPathType
    """Output the noise means"""
    noise_stds: OutputPathType
    """Output the noise standard deviations"""
    free_energy: OutputPathType
    """Output the free energy"""


def fabber_t1_params(
    output: str,
    method: str,
    model: str,
    data: InputPathType,
    data_mult: list[InputPathType] | None = None,
    data_order: str | None = "interleave",
    mask: InputPathType | None = None,
    masked_time_points: list[float] | None = None,
    supp_data: InputPathType | None = None,
    overwrite: bool = False,
    link_to_latest: bool = False,
    simple_output: bool = False,
    load_models: InputPathType | None = None,
    evaluate: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | None = None,
    dump_param_names: bool = False,
    save_model_fit: bool = False,
    save_residuals: bool = False,
    save_model_extras: bool = False,
    save_mvn: bool = False,
    save_mean: bool = False,
    save_std: bool = False,
    save_var: bool = False,
    save_zstat: bool = False,
    save_noise_mean: bool = False,
    save_noise_std: bool = False,
    save_free_energy: bool = False,
    optfile: InputPathType | None = None,
    debug: bool = False,
) -> FabberT1Parameters:
    """
    Build parameters.
    
    Args:
        output: Directory for output files (including logfile).
        method: Inference method to use.
        model: Forward model to use.
        data: Specify a single input data file.
        data_mult: Specify multiple data files for n=1, 2, 3...
        data_order: How multiple data files are handled: concatenate or\
            interleave.
        mask: Mask file. Inference will only be performed where mask value > 0.
        masked_time_points: List of masked time points, indexed from 1. These\
            will be ignored in the parameter updates.
        supp_data: Supplemental timeseries data, required for some models.
        overwrite: Overwrite existing output. If not set, new output\
            directories will be created by appending '+' to the directory name.
        link_to_latest: Try to create a link to the most recent output\
            directory with the prefix _latest.
        simple_output: Simple output format: progress as percentage.
        load_models: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        evaluate: Evaluate model. Set to name of output required or blank for\
            default output.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation - must be consistent\
            with model options where appropriate.
        dump_param_names: Write the file paramnames.txt containing the names of\
            the model parameters.
        save_model_fit: Output the model prediction as a 4d volume.
        save_residuals: Output the residuals (difference between the data and\
            the model prediction).
        save_model_extras: Output any additional model-specific timeseries data.
        save_mvn: Output the final MVN distributions.
        save_mean: Output the parameter means.
        save_std: Output the parameter standard deviations.
        save_var: Output the parameter variances.
        save_zstat: Output the parameter Zstats.
        save_noise_mean: Output the noise means. The noise distribution\
            inferred is the precision of a Gaussian noise source.
        save_noise_std: Output the noise standard deviations.
        save_free_energy: Output the free energy, if calculated.
        optfile: File containing additional options, one per line, in the same\
            form as specified on the command line.
        debug: Output large amounts of debug information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fabber_t1",
        "output": output,
        "method": method,
        "model": model,
        "data": data,
        "overwrite": overwrite,
        "link_to_latest": link_to_latest,
        "simple_output": simple_output,
        "dump_param_names": dump_param_names,
        "save_model_fit": save_model_fit,
        "save_residuals": save_residuals,
        "save_model_extras": save_model_extras,
        "save_mvn": save_mvn,
        "save_mean": save_mean,
        "save_std": save_std,
        "save_var": save_var,
        "save_zstat": save_zstat,
        "save_noise_mean": save_noise_mean,
        "save_noise_std": save_noise_std,
        "save_free_energy": save_free_energy,
        "debug": debug,
    }
    if data_mult is not None:
        params["data_mult"] = data_mult
    if data_order is not None:
        params["data_order"] = data_order
    if mask is not None:
        params["mask"] = mask
    if masked_time_points is not None:
        params["masked_time_points"] = masked_time_points
    if supp_data is not None:
        params["supp_data"] = supp_data
    if load_models is not None:
        params["load_models"] = load_models
    if evaluate is not None:
        params["evaluate"] = evaluate
    if evaluate_params is not None:
        params["evaluate_params"] = evaluate_params
    if evaluate_nt is not None:
        params["evaluate_nt"] = evaluate_nt
    if optfile is not None:
        params["optfile"] = optfile
    return params


def fabber_t1_cargs(
    params: FabberT1Parameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("fabber_t1")
    cargs.extend([
        "--output",
        params.get("output")
    ])
    cargs.extend([
        "--method",
        params.get("method")
    ])
    cargs.extend([
        "--model",
        params.get("model")
    ])
    cargs.extend([
        "--data",
        execution.input_file(params.get("data"))
    ])
    if params.get("data_mult") is not None:
        cargs.extend([
            "--data<n>",
            *[execution.input_file(f) for f in params.get("data_mult")]
        ])
    if params.get("data_order") is not None:
        cargs.extend([
            "--data-order",
            params.get("data_order")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("masked_time_points") is not None:
        cargs.extend([
            "--mt<n>",
            *map(str, params.get("masked_time_points"))
        ])
    if params.get("supp_data") is not None:
        cargs.extend([
            "--suppdata",
            execution.input_file(params.get("supp_data"))
        ])
    if params.get("overwrite"):
        cargs.append("--overwrite")
    if params.get("link_to_latest"):
        cargs.append("--link-to-latest")
    if params.get("simple_output"):
        cargs.append("--simple-output")
    if params.get("load_models") is not None:
        cargs.extend([
            "--loadmodels",
            execution.input_file(params.get("load_models"))
        ])
    if params.get("evaluate") is not None:
        cargs.extend([
            "--evaluate",
            params.get("evaluate")
        ])
    if params.get("evaluate_params") is not None:
        cargs.extend([
            "--evaluate-params",
            params.get("evaluate_params")
        ])
    if params.get("evaluate_nt") is not None:
        cargs.extend([
            "--evaluate-nt",
            str(params.get("evaluate_nt"))
        ])
    if params.get("dump_param_names"):
        cargs.append("--dump-param-names")
    if params.get("save_model_fit"):
        cargs.append("--save-model-fit")
    if params.get("save_residuals"):
        cargs.append("--save-residuals")
    if params.get("save_model_extras"):
        cargs.append("--save-model-extras")
    if params.get("save_mvn"):
        cargs.append("--save-mvn")
    if params.get("save_mean"):
        cargs.append("--save-mean")
    if params.get("save_std"):
        cargs.append("--save-std")
    if params.get("save_var"):
        cargs.append("--save-var")
    if params.get("save_zstat"):
        cargs.append("--save-zstat")
    if params.get("save_noise_mean"):
        cargs.append("--save-noise-mean")
    if params.get("save_noise_std"):
        cargs.append("--save-noise-std")
    if params.get("save_free_energy"):
        cargs.append("--save-free-energy")
    if params.get("optfile") is not None:
        cargs.extend([
            "--optfile",
            execution.input_file(params.get("optfile"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    return cargs


def fabber_t1_outputs(
    params: FabberT1Parameters,
    execution: Execution,
) -> FabberT1Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FabberT1Outputs(
        root=execution.output_file("."),
        param_names=execution.output_file(params.get("output") + "/paramnames.txt"),
        model_fit=execution.output_file(params.get("output") + "/model_prediction.nii.gz"),
        residuals=execution.output_file(params.get("output") + "/residuals.nii.gz"),
        model_extras=execution.output_file(params.get("output") + "/model_extras.nii.gz"),
        mvn_distributions=execution.output_file(params.get("output") + "/mvn_distributions.nii.gz"),
        param_means=execution.output_file(params.get("output") + "/param_means.nii.gz"),
        param_stds=execution.output_file(params.get("output") + "/param_stds.nii.gz"),
        param_vars=execution.output_file(params.get("output") + "/param_vars.nii.gz"),
        param_zstats=execution.output_file(params.get("output") + "/param_zstats.nii.gz"),
        noise_means=execution.output_file(params.get("output") + "/noise_means.nii.gz"),
        noise_stds=execution.output_file(params.get("output") + "/noise_stds.nii.gz"),
        free_energy=execution.output_file(params.get("output") + "/free_energy.nii.gz"),
    )
    return ret


def fabber_t1_execute(
    params: FabberT1Parameters,
    execution: Execution,
) -> FabberT1Outputs:
    """
    Fabber is a tool for performing model-based analysis of fMRI data, using
    advanced Bayesian inference techniques.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FabberT1Outputs`).
    """
    params = execution.params(params)
    cargs = fabber_t1_cargs(params, execution)
    ret = fabber_t1_outputs(params, execution)
    execution.run(cargs)
    return ret


def fabber_t1(
    output: str,
    method: str,
    model: str,
    data: InputPathType,
    data_mult: list[InputPathType] | None = None,
    data_order: str | None = "interleave",
    mask: InputPathType | None = None,
    masked_time_points: list[float] | None = None,
    supp_data: InputPathType | None = None,
    overwrite: bool = False,
    link_to_latest: bool = False,
    simple_output: bool = False,
    load_models: InputPathType | None = None,
    evaluate: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | None = None,
    dump_param_names: bool = False,
    save_model_fit: bool = False,
    save_residuals: bool = False,
    save_model_extras: bool = False,
    save_mvn: bool = False,
    save_mean: bool = False,
    save_std: bool = False,
    save_var: bool = False,
    save_zstat: bool = False,
    save_noise_mean: bool = False,
    save_noise_std: bool = False,
    save_free_energy: bool = False,
    optfile: InputPathType | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> FabberT1Outputs:
    """
    Fabber is a tool for performing model-based analysis of fMRI data, using
    advanced Bayesian inference techniques.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output: Directory for output files (including logfile).
        method: Inference method to use.
        model: Forward model to use.
        data: Specify a single input data file.
        data_mult: Specify multiple data files for n=1, 2, 3...
        data_order: How multiple data files are handled: concatenate or\
            interleave.
        mask: Mask file. Inference will only be performed where mask value > 0.
        masked_time_points: List of masked time points, indexed from 1. These\
            will be ignored in the parameter updates.
        supp_data: Supplemental timeseries data, required for some models.
        overwrite: Overwrite existing output. If not set, new output\
            directories will be created by appending '+' to the directory name.
        link_to_latest: Try to create a link to the most recent output\
            directory with the prefix _latest.
        simple_output: Simple output format: progress as percentage.
        load_models: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        evaluate: Evaluate model. Set to name of output required or blank for\
            default output.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation - must be consistent\
            with model options where appropriate.
        dump_param_names: Write the file paramnames.txt containing the names of\
            the model parameters.
        save_model_fit: Output the model prediction as a 4d volume.
        save_residuals: Output the residuals (difference between the data and\
            the model prediction).
        save_model_extras: Output any additional model-specific timeseries data.
        save_mvn: Output the final MVN distributions.
        save_mean: Output the parameter means.
        save_std: Output the parameter standard deviations.
        save_var: Output the parameter variances.
        save_zstat: Output the parameter Zstats.
        save_noise_mean: Output the noise means. The noise distribution\
            inferred is the precision of a Gaussian noise source.
        save_noise_std: Output the noise standard deviations.
        save_free_energy: Output the free energy, if calculated.
        optfile: File containing additional options, one per line, in the same\
            form as specified on the command line.
        debug: Output large amounts of debug information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberT1Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_T1_METADATA)
    params = fabber_t1_params(
        output=output,
        method=method,
        model=model,
        data=data,
        data_mult=data_mult,
        data_order=data_order,
        mask=mask,
        masked_time_points=masked_time_points,
        supp_data=supp_data,
        overwrite=overwrite,
        link_to_latest=link_to_latest,
        simple_output=simple_output,
        load_models=load_models,
        evaluate=evaluate,
        evaluate_params=evaluate_params,
        evaluate_nt=evaluate_nt,
        dump_param_names=dump_param_names,
        save_model_fit=save_model_fit,
        save_residuals=save_residuals,
        save_model_extras=save_model_extras,
        save_mvn=save_mvn,
        save_mean=save_mean,
        save_std=save_std,
        save_var=save_var,
        save_zstat=save_zstat,
        save_noise_mean=save_noise_mean,
        save_noise_std=save_noise_std,
        save_free_energy=save_free_energy,
        optfile=optfile,
        debug=debug,
    )
    return fabber_t1_execute(params, execution)


__all__ = [
    "FABBER_T1_METADATA",
    "FabberT1Outputs",
    "FabberT1Parameters",
    "fabber_t1",
    "fabber_t1_params",
]
