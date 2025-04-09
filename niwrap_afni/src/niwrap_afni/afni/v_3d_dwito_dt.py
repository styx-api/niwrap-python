# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_DWITO_DT_METADATA = Metadata(
    id="9a917bfe0fc87dc6e13908baec1679a6c7340c54.boutiques",
    name="3dDWItoDT",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dDwitoDtParameters = typing.TypedDict('V3dDwitoDtParameters', {
    "__STYX_TYPE__": typing.Literal["3dDWItoDT"],
    "gradient_file": InputPathType,
    "dataset": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "automask": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "bmatrix_NZ": typing.NotRequired[InputPathType | None],
    "bmatrix_Z": typing.NotRequired[InputPathType | None],
    "bmatrix_FULL": typing.NotRequired[InputPathType | None],
    "scale_out_1000": bool,
    "bmax_ref": typing.NotRequired[float | None],
    "nonlinear": bool,
    "linear": bool,
    "reweight": bool,
    "max_iter": typing.NotRequired[int | None],
    "max_iter_rw": typing.NotRequired[int | None],
    "eigs": bool,
    "debug_briks": bool,
    "cumulative_wts": bool,
    "verbose": typing.NotRequired[int | None],
    "drive_afni": typing.NotRequired[int | None],
    "sep_dsets": bool,
    "csf_val": typing.NotRequired[float | None],
    "min_bad_md": typing.NotRequired[int | None],
    "csf_fa": typing.NotRequired[float | None],
    "opt": typing.NotRequired[str | None],
    "mean_b0": bool,
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
        "3dDWItoDT": v_3d_dwito_dt_cargs,
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
        "3dDWItoDT": v_3d_dwito_dt_outputs,
    }.get(t)


class V3dDwitoDtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_dwito_dt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset"""


def v_3d_dwito_dt_params(
    gradient_file: InputPathType,
    dataset: InputPathType,
    prefix: str | None = None,
    automask: bool = False,
    mask: InputPathType | None = None,
    bmatrix_nz: InputPathType | None = None,
    bmatrix_z: InputPathType | None = None,
    bmatrix_full: InputPathType | None = None,
    scale_out_1000: bool = False,
    bmax_ref: float | None = None,
    nonlinear: bool = False,
    linear: bool = False,
    reweight: bool = False,
    max_iter: int | None = None,
    max_iter_rw: int | None = None,
    eigs: bool = False,
    debug_briks: bool = False,
    cumulative_wts: bool = False,
    verbose: int | None = None,
    drive_afni: int | None = None,
    sep_dsets: bool = False,
    csf_val: float | None = None,
    min_bad_md: int | None = None,
    csf_fa: float | None = None,
    opt: str | None = None,
    mean_b0: bool = False,
) -> V3dDwitoDtParameters:
    """
    Build parameters.
    
    Args:
        gradient_file: A 1D file of the gradient vectors with lines of ASCII\
            floats (Gxi, Gyi, Gzi) or a 1D file of b-matrix elements.
        dataset: A 3D bucket dataset with Np+1 sub-briks where the first\
            sub-brik is the volume acquired with no diffusion weighting.
        prefix: Output dataset prefix name. Default is 'DT'.
        automask: Mask dataset so that tensors are computed only for\
            high-intensity (presumably brain) voxels.
        mask: Use this dataset as mask to include/exclude voxels.
        bmatrix_nz: Input dataset is b-matrix, not gradient directions, and\
            there is no row of zeros at the top of the file.
        bmatrix_z: Similar to '-bmatrix_NZ' but first row of the file is all\
            zeros.
        bmatrix_full: Same as '-bmatrix_Z' but with a more intuitive name.
        scale_out_1000: Increase output parameters with physical units by\
            multiplying them by 1000.
        bmax_ref: Flag the reference b-value if it is greater than zero.
        nonlinear: Compute iterative solution to avoid negative eigenvalues.\
            This is the default method.
        linear: Compute simple linear solution.
        reweight: Recompute weight factors at end of iterations and restart.
        max_iter: Maximum number of iterations for convergence. Default is 10.
        max_iter_rw: Max number of iterations after reweighting. Default is 5.
        eigs: Compute eigenvalues, eigenvectors, fractional anisotropy, and\
            mean diffusivity in sub-briks 6-19.
        debug_briks: Add sub-briks with error functional, original error,\
            number of steps to convergence, and modeled B0 volume.
        cumulative_wts: Show overall weight factors for each gradient level.
        verbose: Print convergence steps every nnnnn voxels.
        drive_afni: Show convergence graphs every nnnnn voxels. AFNI must have\
            NIML communications on.
        sep_dsets: Save tensor, eigenvalues, vectors, FA, MD in separate\
            datasets.
        csf_val: Assign diffusivity value to DWI data where the mean values for\
            b=0 volumes is less than the mean of the remaining volumes at each\
            voxel.
        min_bad_md: Change the min MD value used as a 'badness check' for\
            tensor fits.
        csf_fa: Assign a specific FA value to CSF voxels.
        opt: Optimization method: 'powell', 'gradient', or 'hybrid'.
        mean_b0: Use mean of all b=0 volumes for linear computation and initial\
            linear for nonlinear method.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dDWItoDT",
        "gradient_file": gradient_file,
        "dataset": dataset,
        "automask": automask,
        "scale_out_1000": scale_out_1000,
        "nonlinear": nonlinear,
        "linear": linear,
        "reweight": reweight,
        "eigs": eigs,
        "debug_briks": debug_briks,
        "cumulative_wts": cumulative_wts,
        "sep_dsets": sep_dsets,
        "mean_b0": mean_b0,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if mask is not None:
        params["mask"] = mask
    if bmatrix_nz is not None:
        params["bmatrix_NZ"] = bmatrix_nz
    if bmatrix_z is not None:
        params["bmatrix_Z"] = bmatrix_z
    if bmatrix_full is not None:
        params["bmatrix_FULL"] = bmatrix_full
    if bmax_ref is not None:
        params["bmax_ref"] = bmax_ref
    if max_iter is not None:
        params["max_iter"] = max_iter
    if max_iter_rw is not None:
        params["max_iter_rw"] = max_iter_rw
    if verbose is not None:
        params["verbose"] = verbose
    if drive_afni is not None:
        params["drive_afni"] = drive_afni
    if csf_val is not None:
        params["csf_val"] = csf_val
    if min_bad_md is not None:
        params["min_bad_md"] = min_bad_md
    if csf_fa is not None:
        params["csf_fa"] = csf_fa
    if opt is not None:
        params["opt"] = opt
    return params


def v_3d_dwito_dt_cargs(
    params: V3dDwitoDtParameters,
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
    cargs.append("3dDWItoDT")
    cargs.append(execution.input_file(params.get("gradient_file")))
    cargs.append(execution.input_file(params.get("dataset")))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("bmatrix_NZ") is not None:
        cargs.extend([
            "-bmatrix_NZ",
            execution.input_file(params.get("bmatrix_NZ"))
        ])
    if params.get("bmatrix_Z") is not None:
        cargs.extend([
            "-bmatrix_Z",
            execution.input_file(params.get("bmatrix_Z"))
        ])
    if params.get("bmatrix_FULL") is not None:
        cargs.extend([
            "-bmatrix_FULL",
            execution.input_file(params.get("bmatrix_FULL"))
        ])
    if params.get("scale_out_1000"):
        cargs.append("-scale_out_1000")
    if params.get("bmax_ref") is not None:
        cargs.extend([
            "-bmax_ref",
            str(params.get("bmax_ref"))
        ])
    if params.get("nonlinear"):
        cargs.append("-nonlinear")
    if params.get("linear"):
        cargs.append("-linear")
    if params.get("reweight"):
        cargs.append("-reweight")
    if params.get("max_iter") is not None:
        cargs.extend([
            "-max_iter",
            str(params.get("max_iter"))
        ])
    if params.get("max_iter_rw") is not None:
        cargs.extend([
            "-max_iter_rw",
            str(params.get("max_iter_rw"))
        ])
    if params.get("eigs"):
        cargs.append("-eigs")
    if params.get("debug_briks"):
        cargs.append("-debug_briks")
    if params.get("cumulative_wts"):
        cargs.append("-cumulative_wts")
    if params.get("verbose") is not None:
        cargs.extend([
            "-verbose",
            str(params.get("verbose"))
        ])
    if params.get("drive_afni") is not None:
        cargs.extend([
            "-drive_afni",
            str(params.get("drive_afni"))
        ])
    if params.get("sep_dsets"):
        cargs.append("-sep_dsets")
    if params.get("csf_val") is not None:
        cargs.extend([
            "-csf_val",
            str(params.get("csf_val"))
        ])
    if params.get("min_bad_md") is not None:
        cargs.extend([
            "-min_bad_md",
            str(params.get("min_bad_md"))
        ])
    if params.get("csf_fa") is not None:
        cargs.extend([
            "-csf_fa",
            str(params.get("csf_fa"))
        ])
    if params.get("opt") is not None:
        cargs.extend([
            "-opt",
            params.get("opt")
        ])
    if params.get("mean_b0"):
        cargs.append("-mean_b0")
    return cargs


def v_3d_dwito_dt_outputs(
    params: V3dDwitoDtParameters,
    execution: Execution,
) -> V3dDwitoDtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dDwitoDtOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file("<PREFIX>.*"),
    )
    return ret


def v_3d_dwito_dt_execute(
    params: V3dDwitoDtParameters,
    execution: Execution,
) -> V3dDwitoDtOutputs:
    """
    Computes 6 principal direction tensors from multiple gradient vectors and
    corresponding DTI image volumes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dDwitoDtOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_dwito_dt_cargs(params, execution)
    ret = v_3d_dwito_dt_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_dwito_dt(
    gradient_file: InputPathType,
    dataset: InputPathType,
    prefix: str | None = None,
    automask: bool = False,
    mask: InputPathType | None = None,
    bmatrix_nz: InputPathType | None = None,
    bmatrix_z: InputPathType | None = None,
    bmatrix_full: InputPathType | None = None,
    scale_out_1000: bool = False,
    bmax_ref: float | None = None,
    nonlinear: bool = False,
    linear: bool = False,
    reweight: bool = False,
    max_iter: int | None = None,
    max_iter_rw: int | None = None,
    eigs: bool = False,
    debug_briks: bool = False,
    cumulative_wts: bool = False,
    verbose: int | None = None,
    drive_afni: int | None = None,
    sep_dsets: bool = False,
    csf_val: float | None = None,
    min_bad_md: int | None = None,
    csf_fa: float | None = None,
    opt: str | None = None,
    mean_b0: bool = False,
    runner: Runner | None = None,
) -> V3dDwitoDtOutputs:
    """
    Computes 6 principal direction tensors from multiple gradient vectors and
    corresponding DTI image volumes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        gradient_file: A 1D file of the gradient vectors with lines of ASCII\
            floats (Gxi, Gyi, Gzi) or a 1D file of b-matrix elements.
        dataset: A 3D bucket dataset with Np+1 sub-briks where the first\
            sub-brik is the volume acquired with no diffusion weighting.
        prefix: Output dataset prefix name. Default is 'DT'.
        automask: Mask dataset so that tensors are computed only for\
            high-intensity (presumably brain) voxels.
        mask: Use this dataset as mask to include/exclude voxels.
        bmatrix_nz: Input dataset is b-matrix, not gradient directions, and\
            there is no row of zeros at the top of the file.
        bmatrix_z: Similar to '-bmatrix_NZ' but first row of the file is all\
            zeros.
        bmatrix_full: Same as '-bmatrix_Z' but with a more intuitive name.
        scale_out_1000: Increase output parameters with physical units by\
            multiplying them by 1000.
        bmax_ref: Flag the reference b-value if it is greater than zero.
        nonlinear: Compute iterative solution to avoid negative eigenvalues.\
            This is the default method.
        linear: Compute simple linear solution.
        reweight: Recompute weight factors at end of iterations and restart.
        max_iter: Maximum number of iterations for convergence. Default is 10.
        max_iter_rw: Max number of iterations after reweighting. Default is 5.
        eigs: Compute eigenvalues, eigenvectors, fractional anisotropy, and\
            mean diffusivity in sub-briks 6-19.
        debug_briks: Add sub-briks with error functional, original error,\
            number of steps to convergence, and modeled B0 volume.
        cumulative_wts: Show overall weight factors for each gradient level.
        verbose: Print convergence steps every nnnnn voxels.
        drive_afni: Show convergence graphs every nnnnn voxels. AFNI must have\
            NIML communications on.
        sep_dsets: Save tensor, eigenvalues, vectors, FA, MD in separate\
            datasets.
        csf_val: Assign diffusivity value to DWI data where the mean values for\
            b=0 volumes is less than the mean of the remaining volumes at each\
            voxel.
        min_bad_md: Change the min MD value used as a 'badness check' for\
            tensor fits.
        csf_fa: Assign a specific FA value to CSF voxels.
        opt: Optimization method: 'powell', 'gradient', or 'hybrid'.
        mean_b0: Use mean of all b=0 volumes for linear computation and initial\
            linear for nonlinear method.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDwitoDtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DWITO_DT_METADATA)
    params = v_3d_dwito_dt_params(
        gradient_file=gradient_file,
        dataset=dataset,
        prefix=prefix,
        automask=automask,
        mask=mask,
        bmatrix_nz=bmatrix_nz,
        bmatrix_z=bmatrix_z,
        bmatrix_full=bmatrix_full,
        scale_out_1000=scale_out_1000,
        bmax_ref=bmax_ref,
        nonlinear=nonlinear,
        linear=linear,
        reweight=reweight,
        max_iter=max_iter,
        max_iter_rw=max_iter_rw,
        eigs=eigs,
        debug_briks=debug_briks,
        cumulative_wts=cumulative_wts,
        verbose=verbose,
        drive_afni=drive_afni,
        sep_dsets=sep_dsets,
        csf_val=csf_val,
        min_bad_md=min_bad_md,
        csf_fa=csf_fa,
        opt=opt,
        mean_b0=mean_b0,
    )
    return v_3d_dwito_dt_execute(params, execution)


__all__ = [
    "V3dDwitoDtOutputs",
    "V3dDwitoDtParameters",
    "V_3D_DWITO_DT_METADATA",
    "v_3d_dwito_dt",
    "v_3d_dwito_dt_params",
]
