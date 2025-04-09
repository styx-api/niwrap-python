# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FABBER_METADATA = Metadata(
    id="5d2a0e6b29e70fe10b66108a8eac5087e85c371d.boutiques",
    name="fabber",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FabberParameters = typing.TypedDict('FabberParameters', {
    "__STYX_TYPE__": typing.Literal["fabber"],
    "output": str,
    "method": str,
    "model": str,
    "data_file": InputPathType,
    "data_files": typing.NotRequired[InputPathType | None],
    "data_order": typing.NotRequired[str | None],
    "mask_file": typing.NotRequired[InputPathType | None],
    "mt_n": typing.NotRequired[float | None],
    "supp_data": typing.NotRequired[InputPathType | None],
    "evaluate_output": typing.NotRequired[str | None],
    "evaluate_params": typing.NotRequired[str | None],
    "evaluate_nt": typing.NotRequired[float | None],
    "simple_output": bool,
    "overwrite": bool,
    "link_to_latest": bool,
    "load_models": typing.NotRequired[InputPathType | None],
    "debug": bool,
    "optfile": typing.NotRequired[InputPathType | None],
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
    "help": bool,
    "list_methods": bool,
    "list_models": bool,
    "list_params": bool,
    "desc_params": bool,
    "list_outputs": bool,
    "optfile_1": typing.NotRequired[InputPathType | None],
    "old_optfile": typing.NotRequired[InputPathType | None],
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
        "fabber": fabber_cargs,
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
        "fabber": fabber_outputs,
    }.get(t)


class FabberOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    paramnames_file: OutputPathType
    """File containing the names of the model parameters"""
    model_fit_file: OutputPathType
    """The model fit output file"""
    residuals_file: OutputPathType
    """The residuals output file"""
    model_extras_file: OutputPathType
    """The model extras output file"""
    mvn_file: OutputPathType
    """The MVN distributions output file"""
    mean_file: OutputPathType
    """The parameter means output file"""
    std_file: OutputPathType
    """The parameter standard deviations output file"""
    var_file: OutputPathType
    """The parameter variances output file"""
    zstat_file: OutputPathType
    """The parameter Zstats output file"""
    noise_mean_file: OutputPathType
    """The noise means output file"""
    noise_std_file: OutputPathType
    """The noise standard deviations output file"""
    free_energy_file: OutputPathType
    """The free energy output file"""


def fabber_params(
    output: str,
    method: str,
    model: str,
    data_file: InputPathType,
    data_files: InputPathType | None = None,
    data_order: str | None = "interleave",
    mask_file: InputPathType | None = None,
    mt_n: float | None = None,
    supp_data: InputPathType | None = None,
    evaluate_output: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | None = None,
    simple_output: bool = False,
    overwrite: bool = False,
    link_to_latest: bool = False,
    load_models: InputPathType | None = None,
    debug: bool = False,
    optfile: InputPathType | None = None,
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
    help_: bool = False,
    list_methods: bool = False,
    list_models: bool = False,
    list_params: bool = False,
    desc_params: bool = False,
    list_outputs: bool = False,
    optfile_1: InputPathType | None = None,
    old_optfile: InputPathType | None = None,
) -> FabberParameters:
    """
    Build parameters.
    
    Args:
        output: Directory for output files (including logfile).
        method: Use this inference method.
        model: Use this forward model.
        data_file: Specify a single input data file.
        data_files: Specify multiple data files for n=1, 2, 3...
        data_order: If multiple data files are specified, how they will be\
            handled.
        mask_file: Mask file. Inference will only be performed where mask value\
            > 0.
        mt_n: List of masked time points, indexed from 1. These will be ignored\
            in the parameter updates.
        supp_data: 'Supplemental' timeseries data, required for some models.
        evaluate_output: Evaluate model. Set to name of output required or\
            blank for default output. Requires model configuration options,\
            --evaluate-params and --evaluate-nt.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation.
        simple_output: Instead of usual standard output, simply output series\
            of lines each giving progress as percentage.
        overwrite: If set will overwrite existing output. If not set, new\
            output directories will be created by appending '+' to the directory\
            name.
        link_to_latest: Try to create a link to the most recent output\
            directory with the prefix _latest.
        load_models: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        debug: Output large amounts of debug information. ONLY USE WITH VERY\
            SMALL NUMBERS OF VOXELS.
        optfile: Read options in option=value form from the specified file.
        save_model_fit: Output the model prediction as a 4d volume.
        save_residuals: Output the residuals (difference between the data and\
            the model prediction).
        save_model_extras: Output any additional model-specific timeseries data.
        save_mvn: Output the final MVN distributions.
        save_mean: Output the parameter means.
        save_std: Output the parameter standard deviations.
        save_var: Output the parameter variances.
        save_zstat: Output the parameter Z-stats.
        save_noise_mean: Output the noise means. The noise distribution\
            inferred is the precision of a Gaussian noise source.
        save_noise_std: Output the noise standard deviations.
        save_free_energy: Output the free energy, if calculated.
        help_: Print this usage method. If given with --method or --model,\
            display relevant method/model usage information.
        list_methods: List all known inference methods.
        list_models: List all known forward models.
        list_params: List model parameters (requires model configuration\
            options to be given).
        desc_params: Describe model parameters (name, description, units) -\
            requires model configuration options to be given. Note that not all\
            models provide parameter descriptions.
        list_outputs: List additional model outputs (requires model\
            configuration options to be given).
        optfile_1: Read options in option=value form from the specified file.
        old_optfile: Read options in command line form from the specified file\
            (DEPRECATED).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fabber",
        "output": output,
        "method": method,
        "model": model,
        "data_file": data_file,
        "simple_output": simple_output,
        "overwrite": overwrite,
        "link_to_latest": link_to_latest,
        "debug": debug,
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
        "help": help_,
        "list_methods": list_methods,
        "list_models": list_models,
        "list_params": list_params,
        "desc_params": desc_params,
        "list_outputs": list_outputs,
    }
    if data_files is not None:
        params["data_files"] = data_files
    if data_order is not None:
        params["data_order"] = data_order
    if mask_file is not None:
        params["mask_file"] = mask_file
    if mt_n is not None:
        params["mt_n"] = mt_n
    if supp_data is not None:
        params["supp_data"] = supp_data
    if evaluate_output is not None:
        params["evaluate_output"] = evaluate_output
    if evaluate_params is not None:
        params["evaluate_params"] = evaluate_params
    if evaluate_nt is not None:
        params["evaluate_nt"] = evaluate_nt
    if load_models is not None:
        params["load_models"] = load_models
    if optfile is not None:
        params["optfile"] = optfile
    if optfile_1 is not None:
        params["optfile_1"] = optfile_1
    if old_optfile is not None:
        params["old_optfile"] = old_optfile
    return params


def fabber_cargs(
    params: FabberParameters,
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
    cargs.append("fabber")
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
        execution.input_file(params.get("data_file"))
    ])
    if params.get("data_files") is not None:
        cargs.extend([
            "--data<n>",
            execution.input_file(params.get("data_files"))
        ])
    if params.get("data_order") is not None:
        cargs.extend([
            "--data-order",
            params.get("data_order")
        ])
    if params.get("mask_file") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("mt_n") is not None:
        cargs.extend([
            "--mt<n>",
            str(params.get("mt_n"))
        ])
    if params.get("supp_data") is not None:
        cargs.extend([
            "--suppdata",
            execution.input_file(params.get("supp_data"))
        ])
    if params.get("evaluate_output") is not None:
        cargs.extend([
            "--evaluate",
            params.get("evaluate_output")
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
    if params.get("simple_output"):
        cargs.append("--simple-output")
    if params.get("overwrite"):
        cargs.append("--overwrite")
    if params.get("link_to_latest"):
        cargs.append("--link-to-latest")
    if params.get("load_models") is not None:
        cargs.extend([
            "--loadmodels",
            execution.input_file(params.get("load_models"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("optfile") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("optfile"))
        ])
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
    if params.get("help"):
        cargs.append("--help")
    if params.get("list_methods"):
        cargs.append("--listmethods")
    if params.get("list_models"):
        cargs.append("--listmodels")
    if params.get("list_params"):
        cargs.append("--listparams")
    if params.get("desc_params"):
        cargs.append("--descparams")
    if params.get("list_outputs"):
        cargs.append("--listoutputs")
    if params.get("optfile_1") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("optfile_1"))
        ])
    if params.get("old_optfile") is not None:
        cargs.extend([
            "-@",
            execution.input_file(params.get("old_optfile"))
        ])
    return cargs


def fabber_outputs(
    params: FabberParameters,
    execution: Execution,
) -> FabberOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FabberOutputs(
        root=execution.output_file("."),
        paramnames_file=execution.output_file(params.get("output") + "/paramnames.txt"),
        model_fit_file=execution.output_file(params.get("output") + "/model_fit.nii.gz"),
        residuals_file=execution.output_file(params.get("output") + "/residuals.nii.gz"),
        model_extras_file=execution.output_file(params.get("output") + "/model_extras.nii.gz"),
        mvn_file=execution.output_file(params.get("output") + "/mvn.nii.gz"),
        mean_file=execution.output_file(params.get("output") + "/mean.nii.gz"),
        std_file=execution.output_file(params.get("output") + "/std.nii.gz"),
        var_file=execution.output_file(params.get("output") + "/var.nii.gz"),
        zstat_file=execution.output_file(params.get("output") + "/zstat.nii.gz"),
        noise_mean_file=execution.output_file(params.get("output") + "/noise_mean.nii.gz"),
        noise_std_file=execution.output_file(params.get("output") + "/noise_std.nii.gz"),
        free_energy_file=execution.output_file(params.get("output") + "/free_energy.nii.gz"),
    )
    return ret


def fabber_execute(
    params: FabberParameters,
    execution: Execution,
) -> FabberOutputs:
    """
    Fabber is a tool for model-based Bayesian analysis of time-series data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FabberOutputs`).
    """
    params = execution.params(params)
    cargs = fabber_cargs(params, execution)
    ret = fabber_outputs(params, execution)
    execution.run(cargs)
    return ret


def fabber(
    output: str,
    method: str,
    model: str,
    data_file: InputPathType,
    data_files: InputPathType | None = None,
    data_order: str | None = "interleave",
    mask_file: InputPathType | None = None,
    mt_n: float | None = None,
    supp_data: InputPathType | None = None,
    evaluate_output: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | None = None,
    simple_output: bool = False,
    overwrite: bool = False,
    link_to_latest: bool = False,
    load_models: InputPathType | None = None,
    debug: bool = False,
    optfile: InputPathType | None = None,
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
    help_: bool = False,
    list_methods: bool = False,
    list_models: bool = False,
    list_params: bool = False,
    desc_params: bool = False,
    list_outputs: bool = False,
    optfile_1: InputPathType | None = None,
    old_optfile: InputPathType | None = None,
    runner: Runner | None = None,
) -> FabberOutputs:
    """
    Fabber is a tool for model-based Bayesian analysis of time-series data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output: Directory for output files (including logfile).
        method: Use this inference method.
        model: Use this forward model.
        data_file: Specify a single input data file.
        data_files: Specify multiple data files for n=1, 2, 3...
        data_order: If multiple data files are specified, how they will be\
            handled.
        mask_file: Mask file. Inference will only be performed where mask value\
            > 0.
        mt_n: List of masked time points, indexed from 1. These will be ignored\
            in the parameter updates.
        supp_data: 'Supplemental' timeseries data, required for some models.
        evaluate_output: Evaluate model. Set to name of output required or\
            blank for default output. Requires model configuration options,\
            --evaluate-params and --evaluate-nt.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation.
        simple_output: Instead of usual standard output, simply output series\
            of lines each giving progress as percentage.
        overwrite: If set will overwrite existing output. If not set, new\
            output directories will be created by appending '+' to the directory\
            name.
        link_to_latest: Try to create a link to the most recent output\
            directory with the prefix _latest.
        load_models: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        debug: Output large amounts of debug information. ONLY USE WITH VERY\
            SMALL NUMBERS OF VOXELS.
        optfile: Read options in option=value form from the specified file.
        save_model_fit: Output the model prediction as a 4d volume.
        save_residuals: Output the residuals (difference between the data and\
            the model prediction).
        save_model_extras: Output any additional model-specific timeseries data.
        save_mvn: Output the final MVN distributions.
        save_mean: Output the parameter means.
        save_std: Output the parameter standard deviations.
        save_var: Output the parameter variances.
        save_zstat: Output the parameter Z-stats.
        save_noise_mean: Output the noise means. The noise distribution\
            inferred is the precision of a Gaussian noise source.
        save_noise_std: Output the noise standard deviations.
        save_free_energy: Output the free energy, if calculated.
        help_: Print this usage method. If given with --method or --model,\
            display relevant method/model usage information.
        list_methods: List all known inference methods.
        list_models: List all known forward models.
        list_params: List model parameters (requires model configuration\
            options to be given).
        desc_params: Describe model parameters (name, description, units) -\
            requires model configuration options to be given. Note that not all\
            models provide parameter descriptions.
        list_outputs: List additional model outputs (requires model\
            configuration options to be given).
        optfile_1: Read options in option=value form from the specified file.
        old_optfile: Read options in command line form from the specified file\
            (DEPRECATED).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_METADATA)
    params = fabber_params(
        output=output,
        method=method,
        model=model,
        data_file=data_file,
        data_files=data_files,
        data_order=data_order,
        mask_file=mask_file,
        mt_n=mt_n,
        supp_data=supp_data,
        evaluate_output=evaluate_output,
        evaluate_params=evaluate_params,
        evaluate_nt=evaluate_nt,
        simple_output=simple_output,
        overwrite=overwrite,
        link_to_latest=link_to_latest,
        load_models=load_models,
        debug=debug,
        optfile=optfile,
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
        help_=help_,
        list_methods=list_methods,
        list_models=list_models,
        list_params=list_params,
        desc_params=desc_params,
        list_outputs=list_outputs,
        optfile_1=optfile_1,
        old_optfile=old_optfile,
    )
    return fabber_execute(params, execution)


__all__ = [
    "FABBER_METADATA",
    "FabberOutputs",
    "FabberParameters",
    "fabber",
    "fabber_params",
]
