# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PVMFIT_METADATA = Metadata(
    id="2873389b6bc4586f988630b860c7c91d553dc1af.boutiques",
    name="pvmfit",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


PvmfitParameters = typing.TypedDict('PvmfitParameters', {
    "__STYX_TYPE__": typing.Literal["pvmfit"],
    "data_file": InputPathType,
    "mask_file": InputPathType,
    "bvec_file": InputPathType,
    "bval_file": InputPathType,
    "output_basename": typing.NotRequired[str | None],
    "number_of_fibres": typing.NotRequired[float | None],
    "model_type": typing.NotRequired[int | None],
    "fit_all_models": bool,
    "constrained_nonlinear": bool,
    "constrained_nonlinear_f": bool,
    "grid_search": bool,
    "include_noise_floor": bool,
    "save_bic": bool,
    "verbose": bool,
    "help": bool,
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
        "pvmfit": pvmfit_cargs,
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
        "pvmfit": pvmfit_outputs,
    }.get(t)


class PvmfitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pvmfit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Main output file"""
    bic_file: OutputPathType | None
    """Optional: Saved BIC (Bayesian Information Criterion) for certain
    models"""


def pvmfit_params(
    data_file: InputPathType,
    mask_file: InputPathType,
    bvec_file: InputPathType,
    bval_file: InputPathType,
    output_basename: str | None = "pvm",
    number_of_fibres: float | None = 1,
    model_type: int | None = None,
    fit_all_models: bool = False,
    constrained_nonlinear: bool = False,
    constrained_nonlinear_f: bool = False,
    grid_search: bool = False,
    include_noise_floor: bool = False,
    save_bic: bool = False,
    verbose: bool = False,
    help_: bool = False,
) -> PvmfitParameters:
    """
    Build parameters.
    
    Args:
        data_file: Data file.
        mask_file: Mask file.
        bvec_file: B vectors file.
        bval_file: B values file.
        output_basename: Output basename - default='pvm'.
        number_of_fibres: Number of fibres to fit - default=1.
        model_type: Model type: 1 for Ball-Sticks (single-shell), 2 for\
            Ball-Sticks (multi-shells), 4 for Ball-Binghams.
        fit_all_models: Fit all models from 1 up to N fibres and choose the\
            best using BIC.
        constrained_nonlinear: Model1: Apply constrained nonlinear optimization\
            on the diffusivity, volume fractions and their sum.
        constrained_nonlinear_f: Model1: Apply constrained nonlinear\
            optimization on the diffusivity, volume fractions and their sum. Return\
            n fanning angle estimates, using the Hessian of the cost function.
        grid_search: Use grid search (on the fanning eigenvalues). Default=off.
        include_noise_floor: Include noise floor parameter in the model.
        save_bic: Save BIC for certain models.
        verbose: Switch on diagnostic messages.
        help_: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pvmfit",
        "data_file": data_file,
        "mask_file": mask_file,
        "bvec_file": bvec_file,
        "bval_file": bval_file,
        "fit_all_models": fit_all_models,
        "constrained_nonlinear": constrained_nonlinear,
        "constrained_nonlinear_f": constrained_nonlinear_f,
        "grid_search": grid_search,
        "include_noise_floor": include_noise_floor,
        "save_bic": save_bic,
        "verbose": verbose,
        "help": help_,
    }
    if output_basename is not None:
        params["output_basename"] = output_basename
    if number_of_fibres is not None:
        params["number_of_fibres"] = number_of_fibres
    if model_type is not None:
        params["model_type"] = model_type
    return params


def pvmfit_cargs(
    params: PvmfitParameters,
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
    cargs.append("pvmfit")
    cargs.extend([
        "-k",
        execution.input_file(params.get("data_file"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("mask_file"))
    ])
    cargs.extend([
        "-r",
        execution.input_file(params.get("bvec_file"))
    ])
    cargs.extend([
        "-b",
        execution.input_file(params.get("bval_file"))
    ])
    if params.get("output_basename") is not None:
        cargs.extend([
            "-o",
            params.get("output_basename")
        ])
    if params.get("number_of_fibres") is not None:
        cargs.extend([
            "-n",
            str(params.get("number_of_fibres"))
        ])
    if params.get("model_type") is not None:
        cargs.extend([
            "--model",
            str(params.get("model_type"))
        ])
    if params.get("fit_all_models"):
        cargs.append("--all")
    if params.get("constrained_nonlinear"):
        cargs.append("--cnonlinear")
    if params.get("constrained_nonlinear_f"):
        cargs.append("--cnonlinear_F")
    if params.get("grid_search"):
        cargs.append("--gridsearch")
    if params.get("include_noise_floor"):
        cargs.append("--f0")
    if params.get("save_bic"):
        cargs.append("--BIC")
    if params.get("verbose"):
        cargs.append("-V")
    if params.get("help"):
        cargs.append("-h")
    return cargs


def pvmfit_outputs(
    params: PvmfitParameters,
    execution: Execution,
) -> PvmfitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PvmfitOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_basename") + ".nii.gz") if (params.get("output_basename") is not None) else None,
        bic_file=execution.output_file(params.get("output_basename") + "_BIC.nii.gz") if (params.get("output_basename") is not None) else None,
    )
    return ret


def pvmfit_execute(
    params: PvmfitParameters,
    execution: Execution,
) -> PvmfitOutputs:
    """
    Fits diffusion models to multishell DWI data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PvmfitOutputs`).
    """
    params = execution.params(params)
    cargs = pvmfit_cargs(params, execution)
    ret = pvmfit_outputs(params, execution)
    execution.run(cargs)
    return ret


def pvmfit(
    data_file: InputPathType,
    mask_file: InputPathType,
    bvec_file: InputPathType,
    bval_file: InputPathType,
    output_basename: str | None = "pvm",
    number_of_fibres: float | None = 1,
    model_type: int | None = None,
    fit_all_models: bool = False,
    constrained_nonlinear: bool = False,
    constrained_nonlinear_f: bool = False,
    grid_search: bool = False,
    include_noise_floor: bool = False,
    save_bic: bool = False,
    verbose: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> PvmfitOutputs:
    """
    Fits diffusion models to multishell DWI data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        data_file: Data file.
        mask_file: Mask file.
        bvec_file: B vectors file.
        bval_file: B values file.
        output_basename: Output basename - default='pvm'.
        number_of_fibres: Number of fibres to fit - default=1.
        model_type: Model type: 1 for Ball-Sticks (single-shell), 2 for\
            Ball-Sticks (multi-shells), 4 for Ball-Binghams.
        fit_all_models: Fit all models from 1 up to N fibres and choose the\
            best using BIC.
        constrained_nonlinear: Model1: Apply constrained nonlinear optimization\
            on the diffusivity, volume fractions and their sum.
        constrained_nonlinear_f: Model1: Apply constrained nonlinear\
            optimization on the diffusivity, volume fractions and their sum. Return\
            n fanning angle estimates, using the Hessian of the cost function.
        grid_search: Use grid search (on the fanning eigenvalues). Default=off.
        include_noise_floor: Include noise floor parameter in the model.
        save_bic: Save BIC for certain models.
        verbose: Switch on diagnostic messages.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PvmfitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PVMFIT_METADATA)
    params = pvmfit_params(
        data_file=data_file,
        mask_file=mask_file,
        bvec_file=bvec_file,
        bval_file=bval_file,
        output_basename=output_basename,
        number_of_fibres=number_of_fibres,
        model_type=model_type,
        fit_all_models=fit_all_models,
        constrained_nonlinear=constrained_nonlinear,
        constrained_nonlinear_f=constrained_nonlinear_f,
        grid_search=grid_search,
        include_noise_floor=include_noise_floor,
        save_bic=save_bic,
        verbose=verbose,
        help_=help_,
    )
    return pvmfit_execute(params, execution)


__all__ = [
    "PVMFIT_METADATA",
    "PvmfitOutputs",
    "PvmfitParameters",
    "pvmfit",
    "pvmfit_params",
]
